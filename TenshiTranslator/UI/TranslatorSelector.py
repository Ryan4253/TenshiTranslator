from TenshiTranslator.UI.TimeoutSlider import TimeoutSlider
from TenshiTranslator.UI.BatchSizeSlider import BatchSizeSlider

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt

class TranslatorSelector(QWidget):
    """ A widget that allows the user to select the translator and relevant configuration
    """

    def __init__(self):
        """ Initializes the widget with buttons to select the translator and sliders to configure the translator.
        """

        super().__init__()

        self.buildButtonWidget()
        self.buildSliderWidget()
        
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.buttonLayout)
        self.layout.addWidget(self.stackedWidget)
        self.layout.addItem(QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(self.layout)
        self.toggle(0)

    def buildButtonWidget(self):
        """ Builds the buttons to select the translator.
        """

        self.onlineButton = QPushButton("Online")
        self.offlineButton = QPushButton("Offline")
        self.batchButton = QPushButton("Batch")

        self.onlineButton.setCheckable(True)
        self.offlineButton.setCheckable(True)
        self.batchButton.setCheckable(True)

        self.onlineButton.clicked.connect(lambda: self.toggle(0))
        self.offlineButton.clicked.connect(lambda: self.toggle(1))
        self.batchButton.clicked.connect(lambda: self.toggle(2))
        
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.onlineButton)
        self.buttonLayout.addWidget(self.offlineButton)
        self.buttonLayout.addWidget(self.batchButton)

    def buildSliderWidget(self):
        """ Builds the sliders to configure the translator.
        """

        self.onlineWidget = QWidget()
        self.onlineLayout = QVBoxLayout(self.onlineWidget)
        self.onlineLabel = QLabel("Timeout (s)")
        self.timeoutSlider = TimeoutSlider()
        self.onlineLayout.addWidget(self.onlineLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        self.onlineLayout.addWidget(self.timeoutSlider)
        
        self.offlineWidget = QWidget()
        
        self.batchWidget = QWidget()
        self.batchLayout = QVBoxLayout(self.batchWidget)
        self.batchLabel = QLabel("Batch Size")
        self.batchSizeSlider = BatchSizeSlider()
        self.batchLayout.addWidget(self.batchLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        self.batchLayout.addWidget(self.batchSizeSlider)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.onlineWidget)
        self.stackedWidget.addWidget(self.offlineWidget)
        self.stackedWidget.addWidget(self.batchWidget)

    def toggle(self, index: int):
        """ Toggles the selected translator.

        :param index: the index of the translator to select
        """

        self.onlineButton.setChecked(index == 0)
        self.offlineButton.setChecked(index == 1)
        self.batchButton.setChecked(index == 2)
        self.stackedWidget.setCurrentIndex(index)

    def getTranslator(self) -> str:
        """ Gets the selected translator.

        :return: the selected translator
        """

        if self.onlineButton.isChecked():
            return "Online"
        
        if self.offlineButton.isChecked():
            return "Offline"
        
        if self.batchButton.isChecked():
            return "Batch"
        
        return None
        
    def getTimeout(self) -> int:
        """ Gets the selected timeout.

        :return: the selected timeout
        """

        return self.timeoutSlider.getTimeout()
    
    def getBatchSize(self) -> int:
        """ Gets the selected batch size.
        
        :return: the selected batch size
        """

        return int(self.batchSizeSlider.getBatchSize())