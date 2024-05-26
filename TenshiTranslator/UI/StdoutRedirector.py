from multiprocessing import Queue

class StdoutRedirector:
    """ Redirects the standard output to a buffer.
    """

    def __init__(self, outputBuffer: Queue):
        """ Initializes the redirector with the given output buffer.
        """

        self.outputBuffer = outputBuffer

    def write(self, text: str):
        """ Writes the given text to the output buffer.
        """
        
        if text.strip() != "":
            self.outputBuffer.put(text)

    def flush(self):
        pass