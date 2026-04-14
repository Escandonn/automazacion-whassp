# main.py
# pip install pyside6

import sys
import random
from datetime import datetime

from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QPlainTextEdit,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


# -----------------------------
# Worker de ejemplo (simula bot)
# -----------------------------
class BotWorker(QThread):
    log_signal = Signal(int, str)
    status_signal = Signal(int, str, str)

    def __init__(self, bot_id: int):
        super().__init__()
        self.bot_id = bot_id
        self.running = True

    def run(self):
        pasos = [
            "Abriendo Brave...",
            "Cargando WhatsApp Web...",
            "Verificando sesión activa...",
            "Escaneando chats...",
            "Esperando mensajes..."
        ]

        for paso in pasos:
            if not self.running:
                break
            self.log_signal.emit(self.bot_id, paso)
            self.status_signal.emit(self.bot_id, "Activo", paso)
            self.sleep(random.randint(1, 2))

        if self.running:
            self.log_signal.emit(self.bot_id, "Bot listo y operativo.")
            self.status_signal.emit(self.bot_id, "Activo", "En ejecución")

    def stop(self):
        self.running = False


# -----------------------------
# Main Window
# -----------------------------
class BotFarmUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Granja de Bots")
        self.resize(1200, 700)

        self.total_bots = 2
        self.active_workers = {}

        self.setup_ui()

    # -----------------------------
    # UI Layout
    # -----------------------------
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        # Header Stats
        stats_layout = QHBoxLayout()

        self.lbl_total = self.create_stat_card("Bots Disponibles", str(self.total_bots))
        self.lbl_active = self.create_stat_card("Bots Activos", "0")
        self.lbl_status = self.create_stat_card("Estado Global", "Detenido")

        stats_layout.addWidget(self.lbl_total)
        stats_layout.addWidget(self.lbl_active)
        stats_layout.addWidget(self.lbl_status)

        main_layout.addLayout(stats_layout)

        # Controls
        controls_box = QGroupBox("Controles")
        controls_layout = QHBoxLayout()

        self.btn_start_one = QPushButton("Iniciar 1 Bot")
        self.btn_start_one.clicked.connect(lambda: self.start_bots(1))

        self.spin_multi = QSpinBox()
        self.spin_multi.setRange(1, self.total_bots)
        self.spin_multi.setValue(2)

        self.btn_start_multi = QPushButton("Iniciar Varios")
        self.btn_start_multi.clicked.connect(
            lambda: self.start_bots(self.spin_multi.value())
        )

        self.btn_start_all = QPushButton("Iniciar Todos")
        self.btn_start_all.clicked.connect(lambda: self.start_bots(self.total_bots))

        self.btn_stop_all = QPushButton("Detener Todo")
        self.btn_stop_all.clicked.connect(self.stop_all_bots)

        controls_layout.addWidget(self.btn_start_one)
        controls_layout.addWidget(self.spin_multi)
        controls_layout.addWidget(self.btn_start_multi)
        controls_layout.addWidget(self.btn_start_all)
        controls_layout.addWidget(self.btn_stop_all)

        controls_box.setLayout(controls_layout)
        main_layout.addWidget(controls_box)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "Bot",
            "Estado",
            "Navegador",
            "Paso Actual",
            "Última Acción"
        ])
        self.table.setRowCount(self.total_bots)

        for i in range(self.total_bots):
            self.table.setItem(i, 0, QTableWidgetItem(f"Bot {i+1}"))
            self.table.setItem(i, 1, QTableWidgetItem("Inactivo"))
            self.table.setItem(i, 2, QTableWidgetItem("-"))
            self.table.setItem(i, 3, QTableWidgetItem("Esperando"))
            self.table.setItem(i, 4, QTableWidgetItem("-"))

        main_layout.addWidget(self.table)

        # Logs
        log_box = QGroupBox("Logs en Tiempo Real")
        log_layout = QVBoxLayout()

        self.log_panel = QPlainTextEdit()
        self.log_panel.setReadOnly(True)

        log_layout.addWidget(self.log_panel)
        log_box.setLayout(log_layout)

        main_layout.addWidget(log_box)

        self.apply_styles()

    # -----------------------------
    # Cards de estadísticas
    # -----------------------------
    def create_stat_card(self, title, value):
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)

        layout = QVBoxLayout(card)

        lbl_title = QLabel(title)
        lbl_title.setAlignment(Qt.AlignCenter)

        lbl_value = QLabel(value)
        lbl_value.setAlignment(Qt.AlignCenter)
        lbl_value.setObjectName("statValue")

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_value)

        card.value_label = lbl_value
        return card

    # -----------------------------
    # Bot Logic
    # -----------------------------
    def start_bots(self, cantidad):
        disponibles = [
            i for i in range(self.total_bots)
            if i not in self.active_workers
        ]

        for bot_index in disponibles[:cantidad]:
            worker = BotWorker(bot_index + 1)
            worker.log_signal.connect(self.add_log)
            worker.status_signal.connect(self.update_bot_status)
            worker.start()

            self.active_workers[bot_index] = worker

            self.update_bot_status(bot_index + 1, "Activo", "Inicializando")
            self.add_log(bot_index + 1, "Bot iniciado.")

        self.refresh_stats()

    def stop_all_bots(self):
        for worker in self.active_workers.values():
            worker.stop()
            worker.quit()
            worker.wait()

        self.active_workers.clear()

        for i in range(self.total_bots):
            self.table.setItem(i, 1, QTableWidgetItem("Inactivo"))
            self.table.setItem(i, 2, QTableWidgetItem("-"))
            self.table.setItem(i, 3, QTableWidgetItem("Detenido"))
            self.table.setItem(i, 4, QTableWidgetItem(self.now()))

        self.add_log(0, "Todos los bots detenidos.")
        self.refresh_stats()

    # -----------------------------
    # UI Updates
    # -----------------------------
    def update_bot_status(self, bot_id, estado, paso):
        row = bot_id - 1

        self.table.setItem(row, 1, QTableWidgetItem(estado))
        self.table.setItem(row, 2, QTableWidgetItem(f"Brave #{bot_id}"))
        self.table.setItem(row, 3, QTableWidgetItem(paso))
        self.table.setItem(row, 4, QTableWidgetItem(self.now()))

    def add_log(self, bot_id, message):
        prefix = f"[Bot {bot_id}]" if bot_id else "[SYSTEM]"
        self.log_panel.appendPlainText(
            f"{self.now()} {prefix} {message}"
        )

    def refresh_stats(self):
        self.lbl_active.value_label.setText(str(len(self.active_workers)))

        if len(self.active_workers) == 0:
            self.lbl_status.value_label.setText("Detenido")
        else:
            self.lbl_status.value_label.setText("Ejecutando")

    def now(self):
        return datetime.now().strftime("%H:%M:%S")

    # -----------------------------
    # Styling
    # -----------------------------
    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background: #121212;
            }

            QLabel {
                color: white;
                font-size: 14px;
            }

            #statValue {
                font-size: 24px;
                font-weight: bold;
                color: #00d084;
            }

            QFrame {
                background: #1e1e1e;
                border-radius: 12px;
                padding: 10px;
            }

            QPushButton {
                background: #2563eb;
                color: white;
                border: none;
                padding: 10px 18px;
                border-radius: 8px;
            }

            QPushButton:hover {
                background: #1d4ed8;
            }

            QTableWidget {
                background: #1e1e1e;
                color: white;
                gridline-color: #333;
            }

            QHeaderView::section {
                background: #111827;
                color: white;
                padding: 8px;
            }

            QPlainTextEdit {
                background: #0f172a;
                color: #00ff88;
                border-radius: 8px;
                padding: 8px;
            }

            QGroupBox {
                color: white;
                font-weight: bold;
                border: 1px solid #333;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
        """)


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BotFarmUI()
    window.show()

    sys.exit(app.exec())