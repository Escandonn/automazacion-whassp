from configuracion.selectores import SELECTOR_FILA_CHAT

class EscanerChats:
    """Clase encargada de escanear y localizar los chats en la interfaz."""
    
    def __init__(self, sb):
        self.sb = sb

    def obtener_chats_visibles(self):
        """Devuelve la lista de elementos DOM correspondientes a los chats."""
        return self.sb.find_elements(SELECTOR_FILA_CHAT)
