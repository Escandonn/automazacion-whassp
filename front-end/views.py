import os
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QTabWidget, QFrame, QTableWidget, QTableWidgetItem,
    QHeaderView, QRadioButton, QComboBox, QTextEdit, QLineEdit, QCheckBox,
    QSpinBox, QSizePolicy
)
from PySide6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control Center - WhatsApp Automation")
        self.resize(1100, 750)
        
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(15)
        
        self.setup_header()
        self.setup_tabs()
        
    def setup_header(self):
        self.header_frame = QFrame()
        self.header_frame.setObjectName("headerFrame")
        layout = QHBoxLayout(self.header_frame)
        
        # Title
        title = QLabel("🤖 WhatsApp Bot - Panel de Control")
        title.setObjectName("headerTitle")
        
        # Control Buttons
        self.btn_start = QPushButton("▶ Iniciar Bot")
        self.btn_start.setObjectName("actionPrimary")
        
        self.btn_stop = QPushButton("🛑 Detener Bot")
        self.btn_stop.setObjectName("actionDanger")
        
        self.btn_refresh = QPushButton("🔄 Refrescar Chats")
        self.btn_settings = QPushButton("⚙ Configuración")
        
        # Add to layout
        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_stop)
        layout.addWidget(self.btn_refresh)
        layout.addWidget(self.btn_settings)
        
        self.main_layout.addWidget(self.header_frame)
        
    def setup_tabs(self):
        self.tabs = QTabWidget()
        
        # Create Tabs
        self.tab_dashboard = QWidget()
        self.tab_advanced = QWidget()
        self.tab_logs = QWidget()
        
        self.setup_dashboard_tab()
        self.setup_advanced_tab()
        self.setup_logs_tab()
        
        self.tabs.addTab(self.tab_dashboard, "📊 Dashboard Principal")
        self.tabs.addTab(self.tab_advanced, "⚙️ Automatización Avanzada")
        self.tabs.addTab(self.tab_logs, "📋 Logs y Auditoría")
        
        self.main_layout.addWidget(self.tabs)
        
    def setup_dashboard_tab(self):
        layout = QHBoxLayout(self.tab_dashboard)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)
        
        # Left Column: Session and Chats
        left_col = QVBoxLayout()
        left_col.addWidget(self.create_session_panel())
        left_col.addWidget(self.create_chats_panel())
        
        # Right Column: Response and Execution
        right_col = QVBoxLayout()
        right_col.addWidget(self.create_response_panel())
        right_col.addWidget(self.create_execution_panel())
        
        layout.addLayout(left_col, 60) # 60% width
        layout.addLayout(right_col, 40) # 40% width

    def setup_advanced_tab(self):
        layout = QVBoxLayout(self.tab_advanced)
        layout.setContentsMargins(20, 20, 20, 20)
        
        frame = QFrame()
        grid = QGridLayout(frame)
        grid.setSpacing(15)
        
        title = QLabel("Configuración de Automatización Inteligente")
        title.setObjectName("sectionTitle")
        
        # Form Elements
        self.chk_auto_ia = QCheckBox("Responder Automáticamente con IA (Auto IA ON/OFF)")
        self.chk_responder_1_vez = QCheckBox("Responder Solo 1 Vez (Anti-spam)")
        self.chk_ignorar_grupos = QCheckBox("Ignorar Grupos")
        
        delay_label = QLabel("Delay Random (Anti-ban) seg:")
        self.spin_delay = QSpinBox()
        self.spin_delay.setRange(0, 120)
        self.spin_delay.setValue(5)
        
        rate_limit_label = QLabel("Máx Respuestas por min:")
        self.spin_rate = QSpinBox()
        self.spin_rate.setRange(1, 100)
        self.spin_rate.setValue(10)
        
        # Add to Grid
        grid.addWidget(title, 0, 0, 1, 2)
        grid.addWidget(self.chk_auto_ia, 1, 0, 1, 2)
        grid.addWidget(self.chk_responder_1_vez, 2, 0, 1, 2)
        grid.addWidget(self.chk_ignorar_grupos, 3, 0, 1, 2)
        
        grid.addWidget(delay_label, 4, 0)
        grid.addWidget(self.spin_delay, 4, 1)
        grid.addWidget(rate_limit_label, 5, 0)
        grid.addWidget(self.spin_rate, 5, 1)
        
        grid.setRowStretch(6, 1) # Push to top
        
        layout.addWidget(frame)
        layout.addStretch()

    def setup_logs_tab(self):
        layout = QVBoxLayout(self.tab_logs)
        layout.setContentsMargins(15, 15, 15, 15)
        
        self.logs_table = QTableWidget()
        self.logs_table.setColumnCount(3)
        self.logs_table.setHorizontalHeaderLabels(["Timestamp", "Evento", "Resultado"])
        self.logs_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.logs_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.logs_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        
        # Sample Data
        self._add_log_row("14:22:01", "Chat Detectado: Juan", "OK")
        self._add_log_row("14:22:05", "IA Generó Respuesta", "OK")
        self._add_log_row("14:22:06", "Mensaje Enviado", "OK")
        
        layout.addWidget(self.logs_table)

    def _add_log_row(self, time, event, result):
        row = self.logs_table.rowCount()
        self.logs_table.insertRow(row)
        self.logs_table.setItem(row, 0, QTableWidgetItem(time))
        self.logs_table.setItem(row, 1, QTableWidgetItem(event))
        self.logs_table.setItem(row, 2, QTableWidgetItem(result))

    def create_session_panel(self):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        
        title = QLabel("ESTADO DE SESIÓN")
        title.setObjectName("sectionTitle")
        
        status_layout = QHBoxLayout()
        
        # Badges
        self.badge_brave = QLabel("Brave: Abierto")
        self.badge_brave.setObjectName("badgeSuccess")
        
        self.badge_wa = QLabel("WhatsApp: Listo")
        self.badge_wa.setObjectName("badgeSuccess")
        
        self.badge_login = QLabel("Login: Activa")
        self.badge_login.setObjectName("badgeSuccess")
        
        status_layout.addWidget(self.badge_brave)
        status_layout.addWidget(self.badge_wa)
        status_layout.addWidget(self.badge_login)
        status_layout.addStretch()
        
        info_layout = QHBoxLayout()
        self.lbl_sync = QLabel("Última Sync: 14:22:00")
        self.lbl_uptime = QLabel("Tiempo Activo: 00:45:12")
        info_layout.addWidget(self.lbl_sync)
        info_layout.addWidget(self.lbl_uptime)
        info_layout.addStretch()
        
        layout.addWidget(title)
        layout.addLayout(status_layout)
        layout.addLayout(info_layout)
        return frame

    def create_chats_panel(self):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)
        
        title_box = QWidget()
        title_layout = QHBoxLayout(title_box)
        title_layout.setContentsMargins(10, 10, 10, 0)
        
        title = QLabel("CHATS PENDIENTES")
        title.setObjectName("sectionTitle")
        title_layout.addWidget(title)
        
        layout.addWidget(title_box)
        
        self.chats_table = QTableWidget()
        self.chats_table.setColumnCount(7)
        self.chats_table.setHorizontalHeaderLabels([
            "✔", "Contacto", "Último Mensaje", "Hora", "No Leídos", "Prioridad", "Estado"
        ])
        # Column Resizing
        header = self.chats_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)
        
        # Sample Chat Data
        self._add_chat_row(True, "Juan", "Hola bro", "2:31 PM", "3", "Alta", "Pendiente")
        self._add_chat_row(False, "Empresa X", "Cotización?", "2:28 PM", "1", "Media", "IA Lista")
        
        layout.addWidget(self.chats_table)
        return frame

    def _add_chat_row(self, checked, contact, msg, time, unread, priority, status):
        row = self.chats_table.rowCount()
        self.chats_table.insertRow(row)
        
        # Checkbox Item
        chk_item = QTableWidgetItem()
        chk_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        chk_item.setCheckState(Qt.CheckState.Checked if checked else Qt.CheckState.Unchecked)
        self.chats_table.setItem(row, 0, chk_item)
        
        self.chats_table.setItem(row, 1, QTableWidgetItem(contact))
        self.chats_table.setItem(row, 2, QTableWidgetItem(msg))
        self.chats_table.setItem(row, 3, QTableWidgetItem(time))
        self.chats_table.setItem(row, 4, QTableWidgetItem(unread))
        self.chats_table.setItem(row, 5, QTableWidgetItem(priority))
        self.chats_table.setItem(row, 6, QTableWidgetItem(status))

    def create_response_panel(self):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        
        title = QLabel("CONFIGURACIÓN DE RESPUESTA")
        title.setObjectName("sectionTitle")
        
        # Radios
        radios_layout = QHBoxLayout()
        self.radio_manual = QRadioButton("Manual")
        self.radio_ia = QRadioButton("IA")
        self.radio_template = QRadioButton("Plantilla")
        self.radio_ia.setChecked(True) # Default
        
        radios_layout.addWidget(self.radio_manual)
        radios_layout.addWidget(self.radio_ia)
        radios_layout.addWidget(self.radio_template)
        
        # Template Combo
        self.cmb_template = QComboBox()
        self.cmb_template.addItems(["-- Seleccionar Plantilla --", "Bienvenida", "Despedida", "Soporte"])
        
        # Text Areas
        self.txt_manual = QTextEdit()
        self.txt_manual.setPlaceholderText("Escribe el mensaje manual aquí...")
        self.txt_manual.setMaximumHeight(80)
        
        self.txt_ia = QTextEdit()
        self.txt_ia.setPlaceholderText("Vista previa de IA generada...")
        self.txt_ia.setReadOnly(True)
        self.txt_ia.setText("¡Hola! Claro que sí, en unos minutos te envío la información de los paquetes.")
        
        layout.addWidget(title)
        layout.addLayout(radios_layout)
        layout.addWidget(self.cmb_template)
        layout.addWidget(QLabel("Mensaje Manual:"))
        layout.addWidget(self.txt_manual)
        layout.addWidget(QLabel("Preview Inteligencia Artificial:"))
        layout.addWidget(self.txt_ia)
        
        return frame

    def create_execution_panel(self):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        
        title = QLabel("EJECUCIÓN")
        title.setObjectName("sectionTitle")
        
        self.btn_send_all = QPushButton("Enviar a Todos (Difusión)")
        self.btn_send_all.setObjectName("actionPrimary")
        
        self.btn_send_selected = QPushButton("Enviar a Seleccionados")
        self.btn_schedule = QPushButton("Programar Envío")
        self.btn_retry = QPushButton("Reintentar Fallidos")
        
        layout.addWidget(title)
        layout.addWidget(self.btn_send_all)
        layout.addWidget(self.btn_send_selected)
        layout.addWidget(self.btn_schedule)
        layout.addWidget(self.btn_retry)
        
        return frame
