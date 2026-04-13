from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QTableWidget, QTableWidgetItem

class PanelChatsPendientes(QGroupBox):
    def __init__(self):
        super().__init__("Monitoreo de Chats Pendientes")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.tabla = QTableWidget(0, 5)
        self.tabla.setHorizontalHeaderLabels(["Contacto", "Último Mensaje", "No Leídos", "Prioridad", "Estado"])
        self.layout.addWidget(self.tabla)

    def actualizar_lista(self, chats):
        self.tabla.setRowCount(len(chats))
        for row, chat in enumerate(chats):
            self.tabla.setItem(row, 0, QTableWidgetItem(chat.nombre))
            self.tabla.setItem(row, 1, QTableWidgetItem(chat.ultimo_mensaje))
            self.tabla.setItem(row, 2, QTableWidgetItem(str(chat.no_leidos)))
            self.tabla.setItem(row, 3, QTableWidgetItem("Alta" if chat.no_leidos > 2 else "Media"))
            self.tabla.setItem(row, 4, QTableWidgetItem("Pendiente"))
