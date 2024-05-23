from PyQt6.QtWidgets import QSlider, QToolTip, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QEvent

class TimeoutSlider(QWidget):
    def __init__(self):
        super().__init__()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(int(400 / 5))
        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)
        self.slider.setValue(int(315 / 5))
        self.slider.setMouseTracking(True)
        self.slider.valueChanged.connect(self.updateTooltip)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.slider)

    def event(self, event):
        if event.type() == QEvent.Type.MouseMove or event.type() == QEvent.Type.ToolTip:
            self.updateTooltip()
            
        return super().event(event)

    def updateTooltip(self):
        QToolTip.showText(self.mapToGlobal(self.rect().center()), str(self.getTimeout()))
    
    def getTimeout(self):
        return self.slider.value() * 5