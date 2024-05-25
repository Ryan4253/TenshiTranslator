from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class OutputFormatSelector(QWidget):
    """ A widget that allows the user to select the output format.
    """

    def __init__(self):
        """ Initializes the widget with two buttons to select the output format.
        """

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

    def toggle(self, index: int):
        """ Toggles the selected output format.

        :param index: the index of the selected output format
        """

        self.lineByLine.setChecked(index == 0)
        self.englishOnly.setChecked(index == 1)
    
    def getOutputFormat(self) -> str:
        """ Gets the selected output format.

        :return: the selected output format
        """

        if self.lineByLine.isChecked():
            return "LineByLine"
        
        if self.englishOnly.isChecked():
            return "EnglishOnly"
        
        return None
