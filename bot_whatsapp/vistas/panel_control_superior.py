from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class PanelControlSuperior(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        
        self.btn_iniciar = QPushButton("🟢 Iniciar Bot")
        self.btn_iniciar.clicked.connect(self._on_iniciar)
        
        self.btn_detener = QPushButton("🔴 Detener Bot")
        self.btn_detener.clicked.connect(self._on_detener)
        self.btn_detener.setEnabled(False)
        
        self.btn_refrescar = QPushButton("🔄 Refrescar Chats")
        self.btn_refrescar.clicked.connect(self._on_refrescar)
        
        self.btn_config = QPushButton("⚙ Configuración")
        
        self.layout.addWidget(self.btn_iniciar)
        self.layout.addWidget(self.btn_detener)
        self.layout.addWidget(self.btn_refrescar)
        self.layout.addWidget(self.btn_config)

    def _on_iniciar(self):
        self.btn_iniciar.setEnabled(False)
        self.btn_detener.setEnabled(True)
        self.controlador.iniciar()

    def _on_detener(self):
        self.btn_iniciar.setEnabled(True)
        self.btn_detener.setEnabled(False)
        self.controlador.detener()

    def _on_refrescar(self):
        self.controlador.refrescar_chats_manual()
