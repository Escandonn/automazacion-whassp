import sys
import os

# Asegurar que el directorio de módulos actuales pueda ser importado
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from vistas.interfaz_principal import InterfazPrincipal

def iniciar_aplicacion():
    app = InterfazPrincipal()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()
