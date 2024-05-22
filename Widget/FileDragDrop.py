from Widget.FileFrame import FileFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout
import os

class FileDropWidget(QScrollArea):
    def __init__(self):
        super().__init__()
        self.files = []

        self.container = QWidget()

        self.containerLayout = QVBoxLayout(self.container)
        self.containerLayout.setSpacing(10) 
        self.containerLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setAcceptDrops(True)
        self.setWidgetResizable(True)
        self.setWidget(self.container)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                fileName = url.toLocalFile()
                self.addFile(fileName)

    def addFile(self, fileName: str):
        if fileName in self.files:
            return
        
        if not os.path.isfile(fileName):
            return

        fileFrame = FileFrame(fileName)
        self.containerLayout.addWidget(fileFrame)
        self.files.append(fileName)
        
    def getFiles(self):
        return self.files
    
    def clearFiles(self):
        self.files.clear()
        for i in reversed(range(self.containerLayout.count())):
            self.containerLayout.itemAt(i).widget().setParent(None)