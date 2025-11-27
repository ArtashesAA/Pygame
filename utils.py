import os
import sys

def ruta_relativa(path):
    if hasattr(sys, "_MEIPASS"):
        # Cuando va empaquetado en .exe
        return os.path.join(sys._MEIPASS, path)
    else:
        # Cuando ejecutas normal desde Python
        return os.path.join(path)
