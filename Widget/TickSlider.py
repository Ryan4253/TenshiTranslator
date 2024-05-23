from PyQt6.QtWidgets import QSlider, QToolTip
from PyQt6.QtCore import Qt, QEvent

class LabelSlider(QSlider):
    def __init__(self, labels, default=0):
        super().__init__(Qt.Orientation.Horizontal)
        self.labels = labels
        self.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.setTickInterval(1)
        self.setMinimum(0)
        self.setMaximum(len(labels) - 1)
        self.setSingleStep(1)
        self.setPageStep(1)
        self.setValue(default)
        self.setMouseTracking(True)
        self.valueChanged.connect(self.updateTooltip)

    def event(self, event):
        if event.type() == QEvent.Type.HoverEnter:
            self.updateTooltip(self.value())
        return super().event(event)

    def updateTooltip(self, value):
        QToolTip.showText(self.mapToGlobal(self.rect().center()), self.getValue())
    
    def getValue(self):
        return self.labels[self.value()]