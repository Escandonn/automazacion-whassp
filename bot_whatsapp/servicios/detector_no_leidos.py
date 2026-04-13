class DetectorNoLeidos:
    """Clase para filtrar los chats no leidos a partir de badgets."""
    
    def tiene_no_leidos(self, chat):
        """Retorna True si un chat tiene el marcador de no leídos."""
        return chat.no_leidos > 0
