# WhatsApp Bot - Arquitectura MVC

Este proyecto implementa un bot de WhatsApp Web utilizando Python, automatizado a través de `SeleniumBase` y orquestado mediante el paradigma Orientado a Objetos y una sólida arquitectura MVC (Modelo-Vista-Controlador).

Incluye una interfaz gráfica atractiva construida en `Tkinter` que permite monitorear y gestionar el funcionamiento del bot en tiempo real de forma asíncrona, evitando que la interfaz gráfica se congele mientras el navegador es controlado de forma automatizada.

---

## 🏗️ Arquitectura del Proyecto

A continuación, la estructura de directorios bajo la cual el proyecto está configurado:

```
bot_whatsapp/
│
├── principal.py                         # Punto de entrada de la aplicación
├── README.md
│
├── configuracion/                       # Variables constantes y selectores
│   ├── ajustes.py                       # Caminos de Brave/Chrome y timeouts
│   └── selectores.py                    # CSS Selectors de WhatsApp
│
├── nucleo/                              # Lógica core de infraestructura
│   ├── gestor_navegador.py              # Inicia y detiene SeleniumBase
│   └── sesion_whatsapp.py               # Maneja lógica de inicio de sesión
│
├── modelos/                             # Entidades de dominio
│   └── chat.py                          # Representación de un Chat
│
├── servicios/                           # Casos de uso atómicos
│   ├── escaner_chats.py                 # Encuentra los chats en el DOM
│   └── detector_no_leidos.py            # Analiza un chat en busca de novedades
│
├── controladores/                       # Lógica de interconexión
│   └── controlador_bot.py               # Une lógica UI (vistas) con Servicios
│
└── vistas/                              # Componentes visuales
    └── interfaz_principal.py            # UI de Tkinter
```

---

## 🚀 Instalación y Uso

1. **Dependencias:** Asegúrate de tener instalado `SeleniumBase`:
   ```bash
   pip install seleniumbase
   ```

2. **Ajustes:** Edita el archivo `configuracion/ajustes.py` para asegurar que las constantes `BRAVE_PATH` y `REAL_PROFILE` apununtan a la instalación correcta de tu navegador en tu sistema según el diagrama de arquitectura. 

3. **Ejecutar el bot:**
   Abre una terminal y ejecuta el punto de entrada de la arquitectura:
   ```bash
   python bot_whatsapp/principal.py
   ```

4. **Interfaz:** Se abrirá una ventana de Tkinter con opciones para **Iniciar** y **Detener** el bot, además de visualización de bitácoras y listas de chats priorizados con mensajes nuevos.

---

## 📖 Siguientes Pasos
Este proyecto queda completamente extendible para agregar más lógica robusta:
- Añadir el `ServicioIA` para integrar ChatGPT u otros LLMs como se proyectaba en el archivo original `flujo.md`.
- Adicionar capacidades automáticas o iteraciones conversacionales sin afectar el flujo del loop principal en los controladores.

---
> Proyecto convertido acorde a las mejores prácticas de mantenibilidad MVC!
