import sys
import os
import multiprocessing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TenshiTranslator.UI.MainApplication import MainApplication

from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication([])
    widget = MainApplication()
    widget.show()
    app.exec()