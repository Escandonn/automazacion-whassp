class RegistroProcesados:
    """Clase para evitar envíos dobles o spamming."""
    
    def __init__(self):
        self.procesados = set()

    def marcar_procesado(self, chat):
        print(f"[Mock] RegistroProcesados: Marcando chat de {chat.nombre} como procesado.")
        self.procesados.add(chat.nombre)

    def fue_procesado(self, chat):
        return chat.nombre in self.procesados
