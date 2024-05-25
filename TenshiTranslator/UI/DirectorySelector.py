from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt6.QtCore import Qt

class DirectorySelector(QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.button = QPushButton(title, self)
        self.button.clicked.connect(self.openFileDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def openFileDialog(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.FileMode.Directory)
        fileDialog.setOption(QFileDialog.Option.ShowDirsOnly)

        if fileDialog.exec():
            selected_path = fileDialog.selectedFiles()[0]
            self.button.setToolTip(selected_path)
            self.button.setText('Selected')

    def getDirectory(self):
        if self.button.text() == 'Selected':
            return self.button.toolTip()
    
        return None
