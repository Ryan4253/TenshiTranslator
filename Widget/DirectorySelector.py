from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt6.QtCore import Qt

class DirectorySelector(QWidget):
    def __init__(self, title):
        super().__init__()

        self.button = QPushButton(title, self)
        self.button.clicked.connect(self.openFileDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)


    def openFileDialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.setOption(QFileDialog.Option.ShowDirsOnly)

        if file_dialog.exec():
            selected_path = file_dialog.selectedFiles()[0]
            self.button.setToolTip(selected_path)
            print(f"Selected path: {selected_path}")
            self.button.setText('Selected')

    def getDirectory(self):
        if self.button.text() == 'Selected':
            return self.button.toolTip()
    
        return None
