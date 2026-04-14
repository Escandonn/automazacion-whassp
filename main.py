from seleniumbase import SB
from pathlib import Path
import threading
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QSpinBox, QMessageBox, QHBoxLayout
)

# ==============================
# CONFIGURACIÓN
# ==============================
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

BASE_DIR = Path(__file__).parent

BOT1_PROFILE = BASE_DIR / "sb-personas" / "Profile 1"
BOT2_PROFILE = BASE_DIR / "sb-personas" / "Profile 2"


# ==============================
# BOT 1
# ==============================
def abrir_bot_1():
    with SB(
        browser="chrome",
        binary_location=BRAVE_PATH,
        chromium_arg=f"--user-data-dir={BOT1_PROFILE}"
    ) as sb:
        sb.open("https://web.whatsapp.com")
        sb.sleep(9999)


# ==============================
# BOT 2
# ==============================
def abrir_bot_2():
    with SB(
        browser="chrome",
        binary_location=BRAVE_PATH,
        chromium_arg=f"--user-data-dir={BOT2_PROFILE}"
    ) as sb:
        sb.open("https://web.whatsapp.com")
        sb.sleep(9999)


# ==============================
# INTERFAZ GRÁFICA PYSIDE6
# ==============================
class BotManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Granja de Bots")
        self.resize(300, 150)
        
        # Widget y Layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Etiqueta de información
        self.lbl_disponibles = QLabel("Cantidad de bots disponibles: 2")
        layout.addWidget(self.lbl_disponibles)
        
        # Controles para seleccionar cantidad
        h_layout = QHBoxLayout()
        self.lbl_iniciar = QLabel("Bots a iniciar:")
        self.spin_cantidad = QSpinBox()
        self.spin_cantidad.setMinimum(1)
        self.spin_cantidad.setMaximum(2)
        h_layout.addWidget(self.lbl_iniciar)
        h_layout.addWidget(self.spin_cantidad)
        layout.addLayout(h_layout)
        
        # Botón para iniciar
        self.btn_iniciar = QPushButton("Iniciar Bots")
        self.btn_iniciar.clicked.connect(self.iniciar_bots)
        layout.addWidget(self.btn_iniciar)
        
    def iniciar_bots(self):
        cantidad = self.spin_cantidad.value()
        
        self.btn_iniciar.setEnabled(False)
        self.btn_iniciar.setText("Bots Iniciados...")
        
        if cantidad >= 1:
            threading.Thread(target=abrir_bot_1, daemon=True).start()
        if cantidad == 2:
            threading.Thread(target=abrir_bot_2, daemon=True).start()
            
        QMessageBox.information(self, "Información", f"Se han iniciado {cantidad} bot(s).")


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BotManagerWindow()
    window.show()
    sys.exit(app.exec())