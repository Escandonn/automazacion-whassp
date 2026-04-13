from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QCheckBox

class PanelAutomatizacionAvanzada(QGroupBox):
    def __init__(self):
        super().__init__("Automatización Avanzada")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.chk_auto = QCheckBox("Auto IA ON (Piloto Automático)")
        self.chk_ignorar = QCheckBox("Ignorar Grupos")
        
        self.layout.addWidget(self.chk_auto)
        self.layout.addWidget(self.chk_ignorar)
