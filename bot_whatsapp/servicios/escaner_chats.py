from modelos.chat import Chat
import random

class EscanerChats:
    """Clase para buscar chats en la lista de WhatsApp Web."""
    
    def obtener_chats_visibles(self):
        print("[Mock] EscanerChats: Obteniendo chats visibles...")
        # Generar Mocks (Dummy Data)
        chats_mock = [
            Chat("Empresa X", "Me envias la cotización?", random.randint(1, 3)),
            Chat("Juan Perez", "Hola bro", random.randint(0, 1)),
            Chat("Cliente Nuevo", "Info por favor", random.randint(1, 5)),
            Chat("Martha", "Vale, gracias.", 0)
        ]
        return chats_mock
