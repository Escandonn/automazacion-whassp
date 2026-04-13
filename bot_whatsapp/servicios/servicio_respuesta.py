class ServicioRespuesta:
    """Se encarga de inyectar el texto y enviar el mensaje."""
    
    def enviar_respuesta(self, chat, mensaje):
        print(f"[Mock] ServicioRespuesta: Enviando mensaje a {chat.nombre}: '{mensaje}'")
        return True
