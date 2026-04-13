import sys
import os
from PySide6.QtWidgets import QApplication
from views import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    style_path = os.path.join(script_dir, "styles.qss")
    
    # Load QSS styles
    if os.path.exists(style_path):
        with open(style_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
            
    # Initialize Main Window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
