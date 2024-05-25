from PyQt6.QtWidgets import QSlider, QToolTip, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QEvent

class TimeoutSlider(QWidget):
    """ A slider that allows the user to select the timeout for the translation model.
    """

    def __init__(self):
        """ Initializes the slider with the default timeout of 315 seconds.
        """

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

    def event(self, event: QEvent):
        """ Updates the tooltip when the mouse is moved over the slider.

        :param event: the event that occurred
        """

        if event.type() == QEvent.Type.MouseMove or event.type() == QEvent.Type.ToolTip:
            self.updateTooltip()
            
        return super().event(event)

    def updateTooltip(self):
        """ Updates the tooltip to display the current timeout.
        """

        QToolTip.showText(self.mapToGlobal(self.rect().center()), str(self.getTimeout()))
    
    def getTimeout(self) -> int:
        """ Gets the current timeout selected by the user.

        :return: the current timeout selected by the user
        """

        return self.slider.value() * 5