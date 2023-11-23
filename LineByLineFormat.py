from OutputFormat import OutputFormat
import TextProcessor

class LineByLineFormat(OutputFormat):
    def writeFile(self, outputFilePath: str, japaneseLines: list[str], englishLines: list[str]):
        with open(outputFilePath, 'w', encoding='utf8') as output:
            for japanese, english in zip(japaneseLines, englishLines):
                if TextProcessor.isEmptyLine(japanese):
                    output.write('\n')
                    continue

                if TextProcessor.noJapaneseCharacters(japanese):
                    output.write(japanese)
                    output.write('\n')
                    continue
                    
                output.write(japanese)
                output.write(english)
                output.write('\n\n')