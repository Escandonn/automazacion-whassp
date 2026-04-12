from configuracion.ajustes import WHATSAPP_WEB_URL, ESPERA_CARGA_INICIAL
from configuracion.selectores import SELECTOR_GRILLA_CHATS

class SesionWhatsApp:
    """Maneja la autenticación y carga de la sesión de WhatsApp Web."""
    
    def __init__(self, sb):
        self.sb = sb

    def abrir_whatsapp(self):
        """Abre la URL de WhatsApp Web."""
        self.sb.open(WHATSAPP_WEB_URL)

    def esperar_sesion(self):
        """Espera interactiva a que cargue la lista de chats."""
        self.sb.wait_for_element(SELECTOR_GRILLA_CHATS, timeout=ESPERA_CARGA_INICIAL)
