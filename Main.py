import OnlineTranslator
import FileTranslator

# Driver Code. Modify as needed
if __name__ == "__main__":
    file = "Chapter_1_preview.txt"
    
    # Translate using the online translator
    # start = time.perf_counter()
    OnlineTranslator.translate(file)
    # print(time.perf_counter()-start)

    # Translate using the file translator
    #FileTranslator.preprocessJapanese(file)
    # FileTranslator.postprocessEnglish(file)
    # FileTranslator.mergeOutput(file)  
    # FileTranslator.removeIntermediateFiles(file)
    



