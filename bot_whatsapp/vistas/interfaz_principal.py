import tkinter as tk
from tkinter import messagebox
from controladores.controlador_bot import ControladorBot

class InterfazPrincipal(tk.Tk):
    """Vista principal con Tkinter."""

    def __init__(self):
        super().__init__()
        self.title("Bot de WhatsApp - Arquitectura MVC Avanzada")
        self.geometry("700x700")

        self.controlador = ControladorBot(ui_callback=self.actualizar_vista)
        self.chats_recientes = [] # Cache de los chats detectados

        # Configuración UI
        self._construir_ui()

    def _construir_ui(self):
        # Frame Superior - Controles Principales
        frame_controles = tk.Frame(self, padx=10, pady=10)
        frame_controles.pack(fill=tk.X)

        self.btn_iniciar = tk.Button(frame_controles, text="Iniciar Bot", bg="green", fg="white", font=("Arial", 12, "bold"), command=self._iniciar_bot)
        self.btn_iniciar.pack(side=tk.LEFT, padx=5)

        self.btn_detener = tk.Button(frame_controles, text="Detener Bot", bg="red", fg="white", font=("Arial", 12, "bold"), state=tk.DISABLED, command=self._detener_bot)
        self.btn_detener.pack(side=tk.LEFT, padx=5)
        
        self.btn_ver_chats = tk.Button(frame_controles, text="Refrescar Chats No Respondidos", font=("Arial", 10), command=self._mostrar_chats_no_respondidos)
        self.btn_ver_chats.pack(side=tk.RIGHT, padx=5)

        # Frame Central - Lista de Chats
        frame_lista = tk.LabelFrame(self, text="Chats Pendientes / Monitoreo", padx=10, pady=10)
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_chats = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Consolas", 10))
        self.lista_chats.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista_chats.yview)
        
        self.lista_chats.bind('<<ListboxSelect>>', self._on_select_chat)
        
        # Frame Inferior - Zona de Respuesta
        frame_respuesta = tk.LabelFrame(self, text="Opciones de Respuesta", padx=10, pady=10)
        frame_respuesta.pack(fill=tk.X, padx=10, pady=5)
        
        self.var_usar_ia = tk.BooleanVar(value=False)
        self.chk_ia = tk.Checkbutton(frame_respuesta, text="Generar con IA (Placeholder)", variable=self.var_usar_ia)
        self.chk_ia.pack(anchor=tk.W)

        self.texto_mensaje = tk.Text(frame_respuesta, height=3, font=("Arial", 10))
        self.texto_mensaje.insert(tk.END, "Hola, me encuentro ocupado ahora. Te respondo luego.")
        self.texto_mensaje.pack(fill=tk.X, pady=5)
        
        frame_botones_resp = tk.Frame(frame_respuesta)
        frame_botones_resp.pack(fill=tk.X)
        
        self.btn_enviar_todos = tk.Button(frame_botones_resp, text="Enviar a Todos (Difusión)", bg="#1e90ff", fg="white", font=("Arial", 10, "bold"), command=self._enviar_masivo)
        self.btn_enviar_todos.pack(side=tk.LEFT, padx=5)

        self.btn_enviar_individual = tk.Button(frame_botones_resp, text="Enviar al Seleccionado", state=tk.DISABLED, bg="#ff8c00", fg="white", font=("Arial", 10, "bold"), command=self._enviar_individual)
        self.btn_enviar_individual.pack(side=tk.LEFT, padx=5)

        # Log
        frame_log = tk.LabelFrame(self, text="Registro de Eventos", padx=10, pady=10)
        frame_log.pack(fill=tk.BOTH, expand=False, padx=10, pady=5)
        
        self.log_text = tk.Text(frame_log, height=5, state=tk.DISABLED, font=("Consolas", 9))
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def _iniciar_bot(self):
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_detener.config(state=tk.NORMAL)
        self.controlador.iniciar()

    def _detener_bot(self):
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_detener.config(state=tk.DISABLED)
        self.controlador.detener()

    def _mostrar_chats_no_respondidos(self):
        self.lista_chats.delete(0, tk.END)
        chats_con_mensajes = [c for c in self.chats_recientes if c.tiene_no_leidos]
        
        for chat in chats_con_mensajes:
            self.lista_chats.insert(tk.END, f"🟢 {chat.nombre} - NUEVOS MENSAJES")
        
        if not chats_con_mensajes:
            self.lista_chats.insert(tk.END, "Sin mensajes nuevos por ahora...")

    def _on_select_chat(self, event):
        seleccion = self.lista_chats.curselection()
        if seleccion:
            texto = self.lista_chats.get(seleccion[0])
            if "🟢" in texto:
                self.btn_enviar_individual.config(state=tk.NORMAL)
                return
        self.btn_enviar_individual.config(state=tk.DISABLED)

    def _enviar_masivo(self):
        if not self.controlador.corriendo:
            messagebox.showwarning("Aviso", "Inicia el bot primero.")
            return

        chats_con_mensajes = [c.nombre for c in self.chats_recientes if c.tiene_no_leidos]
        if not chats_con_mensajes:
            messagebox.showinfo("Aviso", "No hay chats sin responder a los que difundir.")
            return

        mensaje = self.texto_mensaje.get("1.0", tk.END).strip()
        if not mensaje:
            messagebox.showwarning("Aviso", "Escribe un mensaje base primero.")
            return
            
        respuesta = messagebox.askyesno("Confirmar", f"¿Enviar el mensaje a los {len(chats_con_mensajes)} chats (Sin IA)?")
        if respuesta:
            self.controlador.enviar_mensaje_masivo(chats_con_mensajes, mensaje)

    def _enviar_individual(self):
        if not self.controlador.corriendo:
            messagebox.showwarning("Aviso", "Inicia el bot primero.")
            return

        seleccion = self.lista_chats.curselection()
        if not seleccion:
            return
            
        texto = self.lista_chats.get(seleccion[0])
        # Extraer el nombre ignorando "🟢 " y " - NUEVOS MENSAJES"
        nombre_chat = texto.replace("🟢 ", "").split(" - NUEVOS MENSAJES")[0].strip()
        
        mensaje = self.texto_mensaje.get("1.0", tk.END).strip()
        usar_ia = self.var_usar_ia.get()
        
        self.controlador.enviar_mensaje_individual(nombre_chat, mensaje, usar_ia)

    def actualizar_vista(self, tipo_mensaje, contenido):
        self.after(0, self._procesar_mensaje, tipo_mensaje, contenido)

    def _procesar_mensaje(self, tipo_mensaje, contenido):
        if tipo_mensaje == "INFO":
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, f"[INFO] {contenido}\n")
            self.log_text.see(tk.END)
            self.log_text.config(state=tk.DISABLED)
        elif tipo_mensaje == "ERROR":
            messagebox.showerror("Error en Bot", contenido)
            self._detener_bot()
        elif tipo_mensaje == "DATA":
            # Almacenamos internamente los chats recibidos para cuando se presione el botón
            self.chats_recientes = contenido

    def on_close(self):
        if self.controlador.corriendo:
            self.controlador.detener()
        self.destroy()
