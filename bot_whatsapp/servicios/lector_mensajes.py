class LectorMensajes:
    """Extrae el texto del último mensaje recibido de un chat específico."""
    
    def leer_ultimo_mensaje(self, chat):
        print(f"[Mock] LectorMensajes: Leyendo el ultimo mensaje de {chat.nombre}...")
        return chat.ultimo_mensaje
