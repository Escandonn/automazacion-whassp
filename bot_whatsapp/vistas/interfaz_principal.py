from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox
from venv import create
from controladores.controlador_bot import ControladorBot
from vistas.panel_control_superior import PanelControlSuperior
from vistas.panel_estado_sesion import PanelEstadoSesion
from vistas.panel_chats_pendientes import PanelChatsPendientes
from vistas.panel_configuracion_respuesta import PanelConfiguracionRespuesta
from vistas.panel_ejecucion import PanelEjecucion
from vistas.panel_automatizacion_avanzada import PanelAutomatizacionAvanzada
from vistas.panel_logs import PanelLogs

class InterfazPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Centro de Control Empresarial WhatsApp")
        self.resize(1000, 700)
        
        self.controlador = ControladorBot(ui_callback=self.actualizar_vista)
        
        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Paneles
        self.panel_control = PanelControlSuperior(self.controlador)
        self.panel_estado = PanelEstadoSesion()
        
        self.zona_central = QHBoxLayout()
        self.columna_izq = QVBoxLayout()
        self.columna_der = QVBoxLayout()
        
        self.panel_chats = PanelChatsPendientes()
        self.panel_config = PanelConfiguracionRespuesta()
        self.panel_ejecucion = PanelEjecucion(self.controlador)
        self.panel_auto = PanelAutomatizacionAvanzada()
        self.panel_logs = PanelLogs()
        
        # Ensamblar Izquierda
        self.columna_izq.addWidget(self.panel_chats)
        self.columna_izq.addWidget(self.panel_logs)
        
        # Ensamblar Derecha
        self.columna_der.addWidget(self.panel_estado)
        self.columna_der.addWidget(self.panel_config)
        self.columna_der.addWidget(self.panel_ejecucion)
        self.columna_der.addWidget(self.panel_auto)
        
        self.zona_central.addLayout(self.columna_izq, 2)
        self.zona_central.addLayout(self.columna_der, 1)
        
        self.main_layout.addWidget(self.panel_control)
        self.main_layout.addLayout(self.zona_central)

    def actualizar_vista(self, tipo_mensaje, contenido):
        # Dispatcher de mensajes desde Controlador
        if tipo_mensaje == "INFO" or tipo_mensaje == "DEBUG":
            self.panel_logs.agregar_log(f"[{tipo_mensaje}] {contenido}")
        elif tipo_mensaje == "ERROR":
            self.panel_logs.agregar_log(f"[ERROR] {contenido}")
            QMessageBox.critical(self, "Error", contenido)
        elif tipo_mensaje == "DATA":
            self.panel_chats.actualizar_lista(contenido)

    def closeEvent(self, event):
        self.controlador.detener()
        event.accept()
