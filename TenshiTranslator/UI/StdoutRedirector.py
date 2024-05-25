class StdoutRedirector:
    def __init__(self, outputBuffer):
        self.outputBuffer = outputBuffer

    def write(self, text):
        if text.strip() != "":
            self.outputBuffer.put(text)

    def flush(self):
        pass