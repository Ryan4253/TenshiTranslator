from multiprocessing import Queue

class StdoutRedirector:
    def __init__(self, outputBuffer: Queue):
        self.outputBuffer = outputBuffer

    def write(self, text):
        if text.strip() != "":
            self.outputBuffer.put(text)

    def flush(self):
        pass