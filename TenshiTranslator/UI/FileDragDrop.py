from TenshiTranslator.UI.FileFrame import FileFrame

import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QMouseEvent
from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QFileDialog, QLabel

class FileDropWidget(QScrollArea):
    """ A widget that allows the user to drag and drop text files to be translated
    """

    def __init__(self):
        """ Initializes the Widget
        """

        super().__init__()
        self.files = []

        self.container = QWidget()

        self.setAcceptDrops(True)
        self.setWidgetResizable(True)
        self.setWidget(self.container)

        self.watermarkLabel = QLabel("Choose a file or drag it here")
        
        self.containerLayout = QVBoxLayout(self.container)
        self.containerLayout.setSpacing(10) 
        self.containerLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.containerLayout.addWidget(self.watermarkLabel)

    def dragEnterEvent(self, event: QDragEnterEvent):
        """ Accepts the event if it contains URLs

        :param event: the drag enter event that occurred
        """

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        """ Adds the files to the list of files to be translated

        :param event: the drop event that occurred
        """

        if event.mimeData().hasUrls():
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                fileName = url.toLocalFile()
                self.addFile(fileName)

    def mousePressEvent(self, event: QMouseEvent):
        """ Opens a file dialog when the user clicks on the widget

        :param event: the mouse event that occurred
        """

        if event.button() == Qt.MouseButton.LeftButton:
            files, _ = QFileDialog.getOpenFileNames(self, "Select Files to Translate", "", "Text Files (*.txt)")
            for file in files:
                self.addFile(file)

    def addFile(self, fileName: str):
        """ Adds a file to the list of files to be translated and hide the watermark if necessary

        :param fileName: path to the file to be added
        """

        if fileName in self.files:
            return
        
        if not os.path.isfile(fileName):
            return
        
        if not fileName.endswith(".txt"):
            return
        
        self.watermarkLabel.hide()
        self.containerLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        fileFrame = FileFrame(fileName)
        self.containerLayout.addWidget(fileFrame)
        self.files.append(fileName)

    def getFiles(self):
        """ Returns the list of files to be translated
        """

        return self.files
    
    def clearFiles(self):
        """ Clears the list of files to be translated
        """

        self.files.clear()
        for i in reversed(range(self.containerLayout.count())):
            if i == 0:
                continue
            self.containerLayout.itemAt(i).widget().setParent(None)

        self.containerLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watermarkLabel.show()

