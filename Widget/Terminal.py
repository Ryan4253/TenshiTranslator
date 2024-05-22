import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QTextCursor
from io import StringIO

class Terminal(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)

    def write(self, text):
        self.insertPlainText(text)
        self.ensureCursorVisible()

    def flush(self):
        pass
