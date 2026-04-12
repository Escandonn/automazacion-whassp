import time
from configuracion.selectores import SELECTOR_INPUT_MENSAJE

class ServicioRespuesta:
    """Encargado de interactuar con la caja de texto y enviar mensajes."""
    
    def __init__(self, sb):
        self.sb = sb

    def enviar_mensaje(self, mensaje):
        """Asume que el chat ya fue clickeado/seleccionado por el navegador, escribe y envía."""
        try:
            self.sb.wait_for_element(SELECTOR_INPUT_MENSAJE, timeout=5)
            # Primero click en la caja de texto
            self.sb.click(SELECTOR_INPUT_MENSAJE)
            # Limpiar por si acaso (opcional)
            
            # Type y mandar con Enter (\n)
            # SB's type command automatically presses Enter if \n is appended
            self.sb.type(SELECTOR_INPUT_MENSAJE, mensaje + "\n")
            
            # Pequeña espera para asegurar que se envió
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error escribiendo mensaje: {e}")
            return False

    def seleccionar_chat(self, elemento_chat):
        """Hace click en un elemento web dado que es la fila del chat."""
        try:
            elemento_chat.click()
            time.sleep(1.5) # Espera a carga del chat central
            return True
        except:
            return False
