from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QPushButton

class PanelEjecucion(QGroupBox):
    def __init__(self, controlador):
        super().__init__("Ejecución")
        self.controlador = controlador
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        
        self.btn_todos = QPushButton("Enviar a Todos")
        self.btn_seleccionado = QPushButton("Enviar Seleccionado")
        self.btn_reintentar = QPushButton("Reintentar Error")
        
        self.layout.addWidget(self.btn_todos)
        self.layout.addWidget(self.btn_seleccionado)
        self.layout.addWidget(self.btn_reintentar)
