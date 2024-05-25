from TenshiTranslator.UI.DirectorySelector import DirectorySelector
from TenshiTranslator.UI.CSVFileSelector import CSVFileSelector
from TenshiTranslator.UI.FileDragDrop import FileDropWidget
from TenshiTranslator.UI.OutputFormatSelector import OutputFormatSelector
from TenshiTranslator.UI.Terminal import Terminal
from TenshiTranslator.UI.TranslatorSelector import TranslatorSelector
from TenshiTranslator.UI.TranslationProcess import TranslationProcess, TranslatorConfig

from TenshiTranslator.Glossary.Glossary import Glossary
from TenshiTranslator.Glossary.CSVGlossary import CSVGlossary
from TenshiTranslator.Glossary.PassthroughGlossary import PassthroughGlossary
from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
from TenshiTranslator.OutputFormat.LineByLineFormat import LineByLineFormat
from TenshiTranslator.OutputFormat.EnglishOnlyFormat import EnglishOnlyFormat

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, QTimer

class MainApplication(QWidget):
    """ The main application window
    """

    def __init__(self):
        """ Initializes the main application window
        """

        super().__init__()
        self.initUI()

        self.process = None
        self.processListener = QTimer()
        self.processListener.timeout.connect(self.listenToProcess)
        self.processListener.start(100)

    def initUI(self):
        """ Initializes the UI of the main application window
        """

        self.setWindowTitle('TenshiTranslator')
        self.setFixedSize(1000, 525)

        self.initLeftUI()
        self.initRightUI()

        layout = QHBoxLayout()
        layout.addWidget(self.left)
        layout.addWidget(self.right)
        self.setLayout(layout)

    def initLeftUI(self):
        """ Initializes the left side of the UI
        """

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

    def initRightUI(self):
        """ Initializes the right side of the UI
        """

        self.fileDropWidget = FileDropWidget()
        self.terminal = Terminal()

        self.right = QWidget()

        rightLayout = QVBoxLayout(self.right)
        rightLayout.addWidget(self.fileDropWidget)
        rightLayout.addWidget(self.terminal)

    def buildTranslatorConfig(self) -> TranslatorConfig:
        """ Builds the translator configuration based on the user input

        :return: the translator configuration
        """

        if self.translatorSelector.getTranslator() != "Online" and self.sugoiSelector.getDirectory() is None:
            self.terminal.write("Please select the Sugoi Translator directory.\n")
            return None
    
        preprocessGlossary = self.buildGlossary(self.preprocessCSVSelector.getDirectory())
        postprocessGlossary = self.buildGlossary(self.postprocessCSVSelector.getDirectory())        
        outputFormat = self.buildOutputFormat(self.outputFormatSelector.getOutputFormat())

        return TranslatorConfig(
            self.translatorSelector.getTranslator(),
            preprocessGlossary,
            postprocessGlossary,
            outputFormat,
            self.sugoiSelector.getDirectory(),
            self.translatorSelector.getTimeout(),
            self.translatorSelector.getBatchSize()
        )

    def buildOutputFormat(self, formatString: str) -> OutputFormat:
        """ Builds the output format based on the selected format string.

        :param formatString: the selected format string
        :return: the output format
        """

        return LineByLineFormat() if formatString == "LineByLine" else EnglishOnlyFormat()
    
    def buildGlossary(self, directory: str) -> Glossary:
        """ Builds the glossary based on the selected directory.

        :param directory: the selected directory
        :return: the glossary
        """

        return CSVGlossary(directory) if directory is not None else PassthroughGlossary()

    def setTranslateButton(self, text: str, color: str, action: callable):
        """ Sets the text, color, and action of the translate button.

        :param text: the text of the button
        :param color: the color of the button
        :param action: the action of the button
        """
        self.translateButton.setText(text)
        self.translateButton.setStyleSheet(f"background-color: {color}")
        self.translateButton.disconnect()
        self.translateButton.clicked.connect(action)

    def listenToProcess(self):
        """ Listens to the translation process and updates the terminal.
        """

        if self.process is None:
            return
        
        while not self.process.getBuffer().empty():
            self.terminal.write(self.process.getBuffer().get() + "\n")

        if self.process is not None and not self.process.is_alive():
            self.onComplete()

    def onTranslate(self):
        """ Handles starting the translation process
        """

        translatorConfig = self.buildTranslatorConfig()
        if translatorConfig is None:
            return
                
        self.process = TranslationProcess(translatorConfig, self.fileDropWidget.getFiles())
        self.process.start()

        self.setTranslateButton("Stop", "red", self.onStop)
 
    def onStop(self):
        """ Handles stopping the translation process
        """

        self.process.terminate()
        self.terminal.write("Translation Stopped\n")
        self.onComplete()

    def onComplete(self):
        """ Handles the completion of the translation process.
        """

        self.process = None    
        self.setTranslateButton("Translate", "", self.onTranslate)

    def onClear(self):
        """ Handles clearing the files and terminal.
        """
        self.fileDropWidget.clearFiles()
        self.terminal.clear()