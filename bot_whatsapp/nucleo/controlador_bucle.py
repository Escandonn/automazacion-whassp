import time
import threading

class ControladorBucle:
    """Clase Mock para manejar el bucle asíncrono o hilo principal de checkeos."""
    def __init__(self, callback):
        self.callback = callback
        self.activo = False
        self.hilo = None

    def iniciar(self):
        self.activo = True
        self.hilo = threading.Thread(target=self._bucle)
        self.hilo.start()

    def detener(self):
        self.activo = False

    def _bucle(self):
        while self.activo:
            self.callback("DEBUG", "[Mock] Ejecutando iteración de escaneo...")
            time.sleep(3) # Ciclo cada 3 segundos
