from PyQt6.QtWidgets import QSlider, QToolTip, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QEvent

class BatchSizeSlider(QWidget):
    """ A slider that allows the user to select the batch size for the translation model.
    """

    def __init__(self):
        """ Initializes the slider with the default batch size of 64.
        """

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

    def event(self, event: QEvent):
        """ Updates the tooltip when the mouse is moved over the slider.

        :param event: the event that occurred
        """

        if event.type() == QEvent.Type.MouseMove or event.type() == QEvent.Type.ToolTip:
            self.updateTooltip()
            
        return super().event(event)

    def updateTooltip(self):
        """ Updates the tooltip to display the current batch size.
        """

        QToolTip.showText(self.mapToGlobal(self.rect().center()), self.getBatchSize())
    
    def getBatchSize(self) -> str:
        """ Gets the current batch size selected by the user.

        :return: the current batch size selected by the user
        """
        
        return self.labels[self.slider.value()]