import sys
from PyQt6.QtWidgets import QPlainTextEdit

class Terminal(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)

    def write(self, text):
        self.insertPlainText(text)
        self.ensureCursorVisible()

    def flush(self):
        pass
