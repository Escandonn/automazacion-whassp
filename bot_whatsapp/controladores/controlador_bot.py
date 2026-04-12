import time
import threading
from modelos.chat import Chat
from nucleo.gestor_navegador import GestorNavegador
from nucleo.sesion_whatsapp import SesionWhatsApp
from servicios.escaner_chats import EscanerChats
from servicios.detector_no_leidos import DetectorNoLeidos
from servicios.servicio_respuesta import ServicioRespuesta
from servicios.servicio_ia import ServicioIA
from configuracion.ajustes import ESPERA_BUCLE

class ControladorBot:
    """Orquesta la ejecución del bot en segundo plano para no bloquear la UI."""
    
    def __init__(self, ui_callback):
        self.ui_callback = ui_callback
        self.corriendo = False
        self.hilo_bot = None
        self.gestor = GestorNavegador()
        self.servicio_ia = ServicioIA()
        self.servicio_respuesta = None # Se inicializará cuando sb esté listo
        
        # Referencias de DOM
        self._escaner = None
        self._detector = None

    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True
            self.hilo_bot = threading.Thread(target=self._bucle_principal, daemon=True)
            self.hilo_bot.start()

    def detener(self):
        self.corriendo = False
        if self.gestor:
            self.gestor.cerrar_navegador()
        self.ui_callback("INFO", "Bot detenido y navegador cerrado.")

    def enviar_mensaje_masivo(self, chats_objetivo, mensaje):
        """Metodo accesible desde UI para disparar mensajes a multiples chats en un hilo separado."""
        def tarea():
            self.ui_callback("INFO", f"Enviando mensaje masivo a {len(chats_objetivo)} chats...")
            for nombre_chat in chats_objetivo:
                self.enviar_mensaje_individual(nombre_chat, mensaje, usar_ia=False)
            self.ui_callback("INFO", "Difusión masiva completada.")
            
        threading.Thread(target=tarea, daemon=True).start()

    def enviar_mensaje_individual(self, nombre_objetivo, mensaje, usar_ia=False):
        """Busca el elemento de chat, lo selecciona y escribe un mensaje."""
        if not self._escaner or not self.servicio_respuesta:
            self.ui_callback("ERROR", "El navegador no está listo para enviar mensajes.")
            return

        def tarea():
            elementos_chat = self._escaner.obtener_chats_visibles()
            chat_encontrado = None
            
            for elemento in elementos_chat:
                nombre = self._detector.obtener_nombre(elemento)
                if nombre == nombre_objetivo:
                    chat_encontrado = elemento
                    break
            
            if chat_encontrado:
                # 1. Seleccionar
                self.servicio_respuesta.seleccionar_chat(chat_encontrado)
                
                # 2. IA / Texto regular
                texto_final = mensaje
                if usar_ia:
                    texto_final = self.servicio_ia.generar_respuesta(nombre_objetivo, mensaje)
                
                # 3. Enviar
                exito = self.servicio_respuesta.enviar_mensaje(texto_final)
                if exito:
                    self.ui_callback("INFO", f"Mensaje enviado con éxito a {nombre_objetivo}.")
                else:
                    self.ui_callback("ERROR", f"Fallo al enviar a {nombre_objetivo}.")
            else:
                self.ui_callback("ERROR", f"No se encontró el chat en pantalla para: {nombre_objetivo}")

        threading.Thread(target=tarea, daemon=True).start()


    def _bucle_principal(self):
        try:
            self.ui_callback("INFO", "Iniciando navegador...")
            sb = self.gestor.abrir_navegador()
            
            sesion = SesionWhatsApp(sb)
            sesion.abrir_whatsapp()
            self.ui_callback("INFO", "Esperando inicio de sesión en WhatsApp...")
            sesion.esperar_sesion()
            self.ui_callback("INFO", "Sesión iniciada con éxito. Escaneando chats...")

            self._escaner = EscanerChats(sb)
            self._detector = DetectorNoLeidos()
            self.servicio_respuesta = ServicioRespuesta(sb)

            while self.corriendo:
                # Leer todos los chats (el scan loop)
                elementos_chat = self._escaner.obtener_chats_visibles()
                
                chats_procesados = []
                for elemento in elementos_chat:
                    nombre = self._detector.obtener_nombre(elemento)
                    tiene_nuevos = self._detector.tiene_no_leidos(elemento)
                    
                    chat = Chat(nombre=nombre, tiene_no_leidos=tiene_nuevos)
                    chats_procesados.append(chat)

                self.ui_callback("DATA", chats_procesados)
                time.sleep(ESPERA_BUCLE)

        except Exception as e:
            self.ui_callback("ERROR", f"Un error ha ocurrido: {str(e)}")
            self.corriendo = False
            self.gestor.cerrar_navegador()
