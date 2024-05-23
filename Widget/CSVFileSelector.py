from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt6.QtCore import Qt

class CSVFileSelector(QWidget):
    def __init__(self, title):
        super().__init__()

        self.button = QPushButton(title, self)
        self.button.clicked.connect(self.openFileDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def openFileDialog(self):
        fileDialog = QFileDialog()
        fileDialog.setNameFilter("CSV File (*.csv)")

        if fileDialog.exec():
            selected_path = fileDialog.selectedFiles()[0]
            self.button.setToolTip(selected_path)
            self.button.setText('Selected')

    def getDirectory(self):
        if self.button.text() == 'Selected':
            return self.button.toolTip()
    
        return None
