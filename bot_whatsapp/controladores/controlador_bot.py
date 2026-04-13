from nucleo.gestor_navegador import GestorNavegador
from nucleo.sesion_whatsapp import SesionWhatsApp
from nucleo.controlador_bucle import ControladorBucle
from servicios.escaner_chats import EscanerChats
from servicios.detector_no_leidos import DetectorNoLeidos
from servicios.servicio_ia import ServicioIA
from servicios.servicio_respuesta import ServicioRespuesta
from servicios.registro_procesados import RegistroProcesados
from controladores.controlador_modo_automatico import ControladorModoAutomatico
from controladores.controlador_modo_semiautomatico import ControladorModoSemiautomatico

class ControladorBot:
    """Orquestador Principal del Sistema MVC."""
    def __init__(self, ui_callback=None):
        self.ui_callback = ui_callback
        
        # Nucleo
        self.gestor = GestorNavegador()
        self.sesion = SesionWhatsApp(self.gestor)
        self.bucle = ControladorBucle(self._on_bucle_tick)
        
        # Servicios
        self.escaner = EscanerChats()
        self.detector = DetectorNoLeidos()
        self.ia = ServicioIA()
        self.respuesta = ServicioRespuesta()
        self.registro = RegistroProcesados()
        
        # Modos
        self.modo_auto = ControladorModoAutomatico(self.escaner, self.detector, self.ia, self.respuesta, self.registro)
        self.modo_semi = ControladorModoSemiautomatico(self.respuesta, self.ia, self)

    def iniciar(self):
        self._emit("INFO", "Iniciando sistema...")
        self.gestor.abrir_navegador()
        self.sesion.abrir_whatsapp()
        if self.sesion.esperar_sesion():
            self._emit("INFO", "Sesion de WhatsApp lista. Iniciando bucle.")
            self.bucle.iniciar()

    def detener(self):
        self._emit("INFO", "Deteniendo bot...")
        self.bucle.detener()
        self.gestor.cerrar_navegador()

    def refrescar_chats_manual(self):
        """Disparado desde UI"""
        chats = self.escaner.obtener_chats_visibles()
        # Filtrar
        pendientes = [c for c in chats if self.detector.tiene_no_leidos(c)]
        self._emit("DATA", pendientes)

    def _on_bucle_tick(self, level, msg):
        self._emit(level, msg)
        # TODO: Aca se inyectaría si está en modo Automatico

    def _emit(self, tipo, contenido):
        if self.ui_callback:
            self.ui_callback(tipo, contenido)
        else:
            print(f"[{tipo}] {contenido}")
