from configuracion.selectores import SELECTOR_MENSAJES_NO_LEIDOS, SELECTOR_TITULO_CHAT

class DetectorNoLeidos:
    """Clase para detectar si un chat tiene mensajes nuevos y extraer su nombre."""
    
    def tiene_no_leidos(self, elemento_chat):
        """Verifica si en el elemento del chat existe el badge de no leídos."""
        try:
            return bool(
                elemento_chat.find_elements(
                    "css selector",
                    SELECTOR_MENSAJES_NO_LEIDOS
                )
            )
        except:
            return False

    def obtener_nombre(self, elemento_chat):
        """Extrae el nombre del chat."""
        try:
            return elemento_chat.find_element(
                "css selector",
                SELECTOR_TITULO_CHAT
            ).get_attribute("title")
        except:
            return "Nombre no encontrado"
