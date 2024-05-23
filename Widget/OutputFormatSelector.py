from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class OutputFormatSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.lineByLine = QPushButton("Line By Line")
        self.lineByLine.setCheckable(True)
        self.lineByLine.setChecked(True)
        self.lineByLine.clicked.connect(self.toggleLineByLine)

        self.englishOnly = QPushButton("English Only")
        self.englishOnly.setCheckable(True)
        self.englishOnly.clicked.connect(self.toggleEnglishOnly)
    
        layout = QHBoxLayout(self)
        layout.addWidget(self.lineByLine)
        layout.addWidget(self.englishOnly)

    def toggleLineByLine(self):
        sender = self.sender()
        self.englishOnly.setChecked(False)
        self.lineByLine.setChecked(True)
    
    def toggleEnglishOnly(self):
        sender = self.sender()
        self.englishOnly.setChecked(True)
        self.lineByLine.setChecked(False)
    
    def getOutputFormat(self):
        if self.lineByLine.isChecked():
            return "LineByLine"
        elif self.englishOnly.isChecked():
            return "EnglishOnly"
        else:
            return None
