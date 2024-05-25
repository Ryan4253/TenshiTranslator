from PyQt6.QtWidgets import QPlainTextEdit

class Terminal(QPlainTextEdit):
    """ A terminal widget that displays text output.
    """

    def __init__(self):
        """ Initializes the terminal.
        """

        super().__init__()
        self.setReadOnly(True)

    def write(self, text: str):
        """ Writes the given text to the terminal.
        """

        self.insertPlainText(text)
        self.ensureCursorVisible()

    def flush(self):
        pass
