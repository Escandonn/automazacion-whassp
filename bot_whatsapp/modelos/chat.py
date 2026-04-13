class Chat:
    """Modelo que representa un chat detectado de WhatsApp."""
    
    def __init__(self, nombre: str, ultimo_mensaje: str = "", no_leidos: int = 0):
        self.nombre = nombre
        self.ultimo_mensaje = ultimo_mensaje
        self.no_leidos = no_leidos

    def __repr__(self):
        return f"<Chat(nombre='{self.nombre}', no_leidos={self.no_leidos})>"
