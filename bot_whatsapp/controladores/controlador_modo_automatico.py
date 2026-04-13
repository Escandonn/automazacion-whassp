from servicios.escaner_chats import EscanerChats
from servicios.detector_no_leidos import DetectorNoLeidos
from servicios.servicio_ia import ServicioIA
from servicios.servicio_respuesta import ServicioRespuesta
from servicios.registro_procesados import RegistroProcesados

class ControladorModoAutomatico:
    """Modo 100% Autónomo."""
    def __init__(self, escaner, detector, ia, respuesta, registro):
        self.escaner = escaner
        self.detector = detector
        self.ia = ia
        self.respuesta = respuesta
        self.registro = registro

    def procesar_automatico(self):
        """Bucle para procesar automáticamente los chats en backend."""
        chats = self.escaner.obtener_chats_visibles()
        for chat in chats:
            if self.detector.tiene_no_leidos(chat) and not self.registro.fue_procesado(chat):
                ai_reply = self.ia.generar_respuesta(chat.ultimo_mensaje)
                self.respuesta.enviar_respuesta(chat, ai_reply)
                self.registro.marcar_procesado(chat)
