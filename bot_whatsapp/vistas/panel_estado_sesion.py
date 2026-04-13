from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QLabel

class PanelEstadoSesion(QGroupBox):
    def __init__(self):
        super().__init__("Estado de WhatsApp")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        
        self.lbl_brave = QLabel("Brave: Cerrado")
        self.lbl_whatsapp = QLabel("WhatsApp: Cargando...")
        self.lbl_login = QLabel("Login: Esperando")
        
        self.layout.addWidget(self.lbl_brave)
        self.layout.addWidget(self.lbl_whatsapp)
        self.layout.addWidget(self.lbl_login)

    def actualizar_estado(self, msg):
        # Aca se interpretan los logs mock de momento
        pass
