from DirectorySelector import DirectorySelector
from CSVFileSelector import CSVFileSelector
from FileDragDrop import FileDropWidget
from OutputFormatSelector import OutputFormatSelector
from Terminal import Terminal
from TranslatorSelector import TranslatorSelector
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class MainApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TenshiTranslator')
        self.setFixedSize(1000, 500)

        self.buildLeftUI()
        self.buildRightUI()

        layout = QHBoxLayout()
        layout.addWidget(self.left)
        layout.addWidget(self.right)
        self.setLayout(layout)

    def buildLeftUI(self):
        self.sugoiLabel = QLabel("Select Sugoi Translator")
        self.sugoiSelector = DirectorySelector("Select")
        self.preprocessCSVLabel = QLabel("Select Preprocess Glossary")
        self.preprocessCSVSelector = CSVFileSelector("Select")
        self.postprocessCSVLabel = QLabel("Select Postprocess Glossary")
        self.postprocessCSVSelector = CSVFileSelector("Select")
        self.translatorLabel = QLabel("Select Translator")
        self.translatorSelector = TranslatorSelector()
        self.outputFormatLabel = QLabel("Select Output Format")
        self.outputFormatSelector = OutputFormatSelector()
        actionWidget = QWidget()
        self.clearButton = QPushButton("Clear")
        self.clearButton.clicked.connect(self.onClear)
        self.translateButton = QPushButton("Translate")
        self.translateButton.clicked.connect(self.onTranslate)
        actionLayout = QHBoxLayout(actionWidget)
        actionLayout.addWidget(self.clearButton)
        actionLayout.addWidget(self.translateButton)

        self.left = QWidget()
        self.left.setFixedWidth(250)

        leftLayout = QVBoxLayout(self.left)
        leftLayout.addWidget(self.sugoiLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        leftLayout.addWidget(self.sugoiSelector)
        leftLayout.addWidget(self.preprocessCSVLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        leftLayout.addWidget(self.preprocessCSVSelector)
        leftLayout.addWidget(self.postprocessCSVLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        leftLayout.addWidget(self.postprocessCSVSelector)
        leftLayout.addWidget(self.translatorLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        leftLayout.addWidget(self.translatorSelector)
        leftLayout.addWidget(self.outputFormatLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        leftLayout.addWidget(self.outputFormatSelector)
        leftLayout.addWidget(actionWidget)

    def buildRightUI(self):
        self.fileDropWidget = FileDropWidget()
        self.terminal = Terminal()

        self.right = QWidget()

        rightLayout = QVBoxLayout(self.right)
        rightLayout.addWidget(self.fileDropWidget)
        rightLayout.addWidget(self.terminal)


    def buildTranslator(self):
        if self.translatorSelector.getTranslator() != "Online" and self.sugoiSelector.getDirectory() is None:
            self.terminal.write("Please select the Sugoi Translator directory.\n")
            return None
    
        return True

    def onTranslate(self):
        translator = self.buildTranslator()
        if translator is None:
            return
        
        self.translateButton.setText("Stop")
        self.translateButton.setStyleSheet("background-color: red")
        self.translateButton.disconnect()
        self.translateButton.clicked.connect(self.onStop)
        
        self.terminal.write("Starting translation...\n")
        # Logic goes here
        
    def onStop(self):
        self.translateButton.setText("Translate")
        self.translateButton.setStyleSheet("")
        self.translateButton.disconnect()
        self.translateButton.clicked.connect(self.onTranslate)

        self.terminal.write("Translation Stopped\n")
        # Logic goes here

    def onComplete(self):
        self.translateButton.setText("Translate")
        self.translateButton.setStyleSheet("")
        self.translateButton.disconnect()
        self.translateButton.clicked.connect(self.onTranslate)
        self.terminal.write("Translation Completed\n")

    def onClear(self):
        self.fileDropWidget.clearFiles()
        self.terminal.clear()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainApplication()
    widget.show()
    app.exec()