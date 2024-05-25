from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt6.QtCore import Qt

class DirectorySelector(QWidget):
    """ A button that allows the user to select a folder.
    """

    def __init__(self, title: str):
        """ Initializes the button with the given title.

        :param title: the title of the button
        """

        super().__init__()

        self.button = QPushButton(title, self)
        self.button.clicked.connect(self.openFileDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def openFileDialog(self):
        """ Opens a file dialog to allow the user to select a folder.
        """

        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.FileMode.Directory)
        fileDialog.setOption(QFileDialog.Option.ShowDirsOnly)

        if fileDialog.exec():
            selected_path = fileDialog.selectedFiles()[0]
            self.button.setToolTip(selected_path)
            self.button.setText('Selected')

    def getDirectory(self) -> str:
        """ Gets the directory of the selected folder, or None if no folder has been selected.

        :return: the directory of the selected folder, or None if no folder has been selected
        """
        
        if self.button.text() == 'Selected':
            return self.button.toolTip()
    
        return None
