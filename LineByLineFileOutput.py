from FileOutput import FileOutput
import TextProcessor

class LineByLineFileOutput(FileOutput):
    def writeOutput(outputFilePath, japaneseLines, englishLines):
        with open(outputFilePath, 'w', encoding='utf8') as output:
            for japanese, english in zip(japaneseLines, englishLines):
                if TextProcessor.isEmptyLine(japanese):
                    output.write('\n')
                    continue

                if not TextProcessor.hasJapaneseCharacters(japanese):
                    output.write(japanese)
                    output.write('\n')
                    continue

                output.write(japanese)
                output.write(english)
                output.write('\n\n')