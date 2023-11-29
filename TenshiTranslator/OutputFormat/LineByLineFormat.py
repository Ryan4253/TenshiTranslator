## @package OutputFormat
#  Contains the EnglishOnlyFormat class

from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
import TenshiTranslator.Util.TextProcessor

## Output format that outputs the japanese lines followed by the translated lines with the following rules:
#  - An empty line between two japanese line and translations
#  - If the japanese line is empty, there will be two empty lines in the output
#  - If the japanese line contains no japanese characters, it will be outputted as is with no translation
#
# This format is intended for translators to quickly reference and check translations
class LineByLineFormat(OutputFormat):
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
                    output.write('\n')
                    continue
                    
                output.write(japanese)
                output.write(english)
                output.write('\n\n')