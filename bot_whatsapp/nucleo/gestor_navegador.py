from seleniumbase import SB
from configuracion.ajustes import BRAVE_PATH, REAL_PROFILE

class GestorNavegador:
    """Clase encargada de manejar el ciclo de vida del navegador con SeleniumBase."""
    
    def __init__(self):
        self.sb = None
        self._context_manager = None

    def abrir_navegador(self):
        self._context_manager = SB(
            browser="chrome",
            binary_location=BRAVE_PATH,
            user_data_dir=REAL_PROFILE,
            maximize=True
        )
        self.sb = self._context_manager.__enter__()
        return self.sb

    def cerrar_navegador(self):
        if self._context_manager:
            self._context_manager.__exit__(None, None, None)
            self._context_manager = None
            self.sb = None
