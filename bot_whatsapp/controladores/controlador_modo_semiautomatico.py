class ControladorModoSemiautomatico:
    """Modo controlado por humano (GUI)."""
    def __init__(self, respuesta, ia, control_bot):
        self.respuesta = respuesta
        self.ia = ia
        self.control = control_bot

    def procesar_chat_manual(self, chat, mensaje_custom, usar_ia=False):
        if usar_ia:
            ai_reply = self.ia.generar_respuesta(chat.ultimo_mensaje)
            self.respuesta.enviar_respuesta(chat, ai_reply)
        else:
            self.respuesta.enviar_respuesta(chat, mensaje_custom)
