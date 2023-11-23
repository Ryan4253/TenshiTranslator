from OutputFormat import OutputFormat
import TextProcessor

class EnglishOnlyFormat(OutputFormat):
    def writeFile(self, outputFilePath, japaneseLines, englishLines):
        with open(outputFilePath, 'w', encoding='utf8') as output:
            for japanese, english in zip(japaneseLines, englishLines):
                if TextProcessor.isEmptyLine(japanese):
                    output.write('\n')
                    continue

                if not TextProcessor.hasJapaneseCharacters(japanese):
                    output.write(japanese)
                    continue
                    
                output.write(english)
                output.write('\n')
        