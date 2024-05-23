from PyQt6.QtWidgets import QSlider, QToolTip, QWidget, QApplication, QVBoxLayout
from PyQt6.QtCore import Qt, QEvent
import sys

class BatchSizeSlider(QWidget):
    def __init__(self):
        super().__init__()
        self.labels = ["2", "4", "8", "16", "32", "64", "128", "256"]
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(len(self.labels) - 1)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)
        self.slider.setValue(5)
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
        QToolTip.showText(self.mapToGlobal(self.rect().center()), self.getBatchSize())
    
    def getBatchSize(self):
        return self.labels[self.slider.value()]
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BatchSizeSlider()
    ex.show()
    sys.exit(app.exec())