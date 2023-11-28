from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
import TenshiTranslator.Util.TextProcessor

class LineByLineFormat(OutputFormat):
    def writeFile(self, outputFilePath: str, japaneseLines: list[str], englishLines: list[str]):
        with open(outputFilePath, 'w', encoding='utf8') as output:
            for japanese, english in zip(japaneseLines, englishLines):
                if TenshiTranslator.Util.TextProcessor.isEmptyLine(japanese):
                    output.write('\n')
                    continue

                if TenshiTranslator.Util.TextProcessor.noJapaneseCharacters(japanese):
                    output.write(japanese)
                    output.write('\n')
                    continue
                    
                output.write(japanese)
                output.write(english)
                output.write('\n\n')