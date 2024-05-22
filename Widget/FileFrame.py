from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QFrame

class FileFrame(QLabel):
    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.file_name = file_name

        self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)
        self.setFixedHeight(50)
        
    def getFileName(self):
        return self.file_name