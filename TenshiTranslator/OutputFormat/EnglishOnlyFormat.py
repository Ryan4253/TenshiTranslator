## @module OutputFormat
#  Contains the EnglishOnlyFormat class

from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
import TenshiTranslator.Util.TextProcessor

## Output format that mimics the structure of the input file, but only contains the translated lines
class EnglishOnlyFormat(OutputFormat):
    ## writes the translated lines to a file. file will be overwritten if it already exists
    #
    #  @param outputFilePath path to the output file
    #  @param japaneseLines list of japanese lines
    #  @param englishLines list of translated lines
    def writeFile(self, outputFilePath: str, japaneseLines: list[str], englishLines: list[str]):
        with open(outputFilePath, 'w', encoding='utf8') as output:
            for japanese, english in zip(japaneseLines, englishLines):
                if TenshiTranslator.Util.TextProcessor.isEmptyLine(japanese):
                    output.write('\n')
                    continue

                if TenshiTranslator.Util.TextProcessor.noJapaneseCharacters(japanese):
                    output.write(japanese)
                    continue
                    
                output.write(english)
                output.write('\n')