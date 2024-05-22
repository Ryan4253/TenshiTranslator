import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

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
    
        layout = QHBoxLayout()
        layout.addWidget(self.lineByLine)
        layout.addWidget(self.englishOnly)

        self.setLayout(layout)

    def toggleLineByLine(self):
        sender = self.sender()
        self.englishOnly.setChecked(False)
        self.lineByLine.setChecked(True)
        print("Line By Line")
    
    def toggleEnglishOnly(self):
        sender = self.sender()
        self.englishOnly.setChecked(True)
        self.lineByLine.setChecked(False)
        print("English Only")
    
    def getOutputFormat(self):
        if self.lineByLine.isChecked():
            return "Line By Line"
        elif self.englishOnly.isChecked():
            return "English Only"
        else:
            return None


# Main part of the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = OutputFormatSelector()
    widget.show()
    sys.exit(app.exec())