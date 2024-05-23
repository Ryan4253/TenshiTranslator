from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class OutputFormatSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.lineByLine = QPushButton("Line By Line")
        self.englishOnly = QPushButton("English Only")

        self.lineByLine.setCheckable(True)
        self.englishOnly.setCheckable(True)

        self.lineByLine.clicked.connect(lambda: self.toggle(0))
        self.englishOnly.clicked.connect(lambda: self.toggle(1))
    
        layout = QHBoxLayout(self)
        layout.addWidget(self.lineByLine)
        layout.addWidget(self.englishOnly)

        self.toggle(0)

    def toggle(self, index):
        self.lineByLine.setChecked(index == 0)
        self.englishOnly.setChecked(index == 1)
    
    def getOutputFormat(self):
        if self.lineByLine.isChecked():
            return "LineByLine"
        
        if self.englishOnly.isChecked():
            return "EnglishOnly"
        
        return None
