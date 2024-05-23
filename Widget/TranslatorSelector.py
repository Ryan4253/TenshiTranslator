from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from TimeoutSlider import TimeoutSlider
from BatchSizeSlider import BatchSizeSlider  

class TranslatorSelector(QWidget):
    def __init__(self):
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
        self.button1 = QPushButton("Online")
        self.button2 = QPushButton("Offline")
        self.button3 = QPushButton("Batch")

        self.button1.setCheckable(True)
        self.button2.setCheckable(True)
        self.button3.setCheckable(True)

        self.button1.clicked.connect(lambda: self.toggle(0))
        self.button2.clicked.connect(lambda: self.toggle(1))
        self.button3.clicked.connect(lambda: self.toggle(2))
        
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.button1)
        self.buttonLayout.addWidget(self.button2)
        self.buttonLayout.addWidget(self.button3)

    def buildSliderWidget(self):
        self.widget1 = QWidget()
        self.widget1Layout = QVBoxLayout(self.widget1)
        self.label1 = QLabel("Timeout (s)")
        self.slider1 = TimeoutSlider()
        self.widget1Layout.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.widget1Layout.addWidget(self.slider1)
        
        self.widget2 = QWidget()
        
        self.widget3 = QWidget()
        self.widget3Layout = QVBoxLayout(self.widget3)
        self.label3 = QLabel("Batch Size")
        self.slider3 = BatchSizeSlider()
        self.widget3Layout.addWidget(self.label3, alignment=Qt.AlignmentFlag.AlignCenter)
        self.widget3Layout.addWidget(self.slider3)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.widget1)
        self.stackedWidget.addWidget(self.widget2)
        self.stackedWidget.addWidget(self.widget3)

    def toggle(self, index):
        self.button1.setChecked(index == 0)
        self.button2.setChecked(index == 1)
        self.button3.setChecked(index == 2)
        self.stackedWidget.setCurrentIndex(index)

    def getTranslator(self):
        if self.button1.isChecked():
            return "Online"
        
        if self.button2.isChecked():
            return "Offline"
        
        if self.button3.isChecked():
            return "Batch"
        
        return None
        
    def getTimeout(self):
        return self.slider1.getTimeout()
    
    def getBatchSize(self):
        return self.slider2.getBatchSize()