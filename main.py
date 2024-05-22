import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QFrame, QScrollArea, QPushButton, QHBoxLayout
import os
from Widget.FileDragDrop import FileDropWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Drag and Drop')
        self.setGeometry(100, 100, 400, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.fileDropWidget = FileDropWidget()
        self.layout.addWidget(self.fileDropWidget)

        self.printButton = QPushButton("Print File List")
        self.printButton.clicked.connect(self.printFileList)
        self.layout.addWidget(self.printButton)

    def printFileList(self):
        print("Dropped Files:")
        for file_name in self.fileDropWidget.getFiles():
            print(file_name)
        self.fileDropWidget.clearFiles()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())