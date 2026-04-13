from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QTextEdit

class PanelLogs(QGroupBox):
    def __init__(self):
        super().__init__("Logs y Trazabilidad")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.texto_logs = QTextEdit()
        self.texto_logs.setReadOnly(True)
        self.layout.addWidget(self.texto_logs)

    def agregar_log(self, mensaje):
        self.texto_logs.append(mensaje)
