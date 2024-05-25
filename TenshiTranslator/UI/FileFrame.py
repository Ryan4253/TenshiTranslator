from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QFrame

class FileFrame(QLabel):
    def __init__(self, fileName: str):
        """ Initializes the frame with the given file name.
        """

        super().__init__(fileName)
        self.fileName = fileName

        self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)
        self.setFixedHeight(50)
        
    def getFileName(self) -> str:
        """ Gets the file name of the frame.

        :return: the file name of the frame
        """

        return self.fileName