from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QRadioButton, QTextEdit

class PanelConfiguracionRespuesta(QGroupBox):
    def __init__(self):
        super().__init__("Configuración de Mensaje")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.radio_manual = QRadioButton("Modo Manual")
        self.radio_ia = QRadioButton("Modo IA")
        self.radio_manual.setChecked(True)
        
        self.texto = QTextEdit()
        self.texto.setPlaceholderText("Escribe el mensaje aquí...")
        
        self.layout.addWidget(self.radio_manual)
        self.layout.addWidget(self.radio_ia)
        self.layout.addWidget(self.texto)

    def obtener_mensaje(self):
        return self.texto.toPlainText()
    
    def usa_ia(self):
        return self.radio_ia.isChecked()
