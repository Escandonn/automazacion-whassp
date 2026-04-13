import sys
from PySide6.QtWidgets import QApplication
from vistas.interfaz_principal import InterfazPrincipal

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion") # Estilo más moderno por defecto
    ventana = InterfazPrincipal()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
