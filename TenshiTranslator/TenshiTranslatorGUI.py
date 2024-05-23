import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TenshiTranslator.UI.MainApplication import MainApplication

from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    widget = MainApplication()
    widget.show()
    app.exec()