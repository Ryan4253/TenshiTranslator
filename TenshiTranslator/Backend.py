import sys
import argparse
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TenshiTranslator.Util.Glossary import Glossary
from TenshiTranslator.OutputFormat.LineByLineFormat import LineByLineFormat
from TenshiTranslator.OutputFormat.EnglishOnlyFormat import EnglishOnlyFormat
from TenshiTranslator.Translator.OnlineTranslator import OnlineTranslator
from TenshiTranslator.Translator.BatchTranslator import BatchTranslator
from TenshiTranslator.Translator.OfflineTranslator import OfflineTranslator

def directory(directory):
    if os.path.isdir(directory):
        return directory
    else:
        raise NotADirectoryError(directory)

parser = argparse.ArgumentParser(description='TenshiTranslator Backend')
parser.add_argument('Translator', type=str, help='Type of translator to use', choices=['Online', 'Offline', 'Batch'])
parser.add_argument('OutputFormat', type=str, help='Output format to use', choices=['LineByLine', 'EnglishOnly'])
parser.add_argument('GlossaryNames', type=str, help='File path to the glossary names file')
parser.add_argument('GlossaryCorrections', type=str, help='File path to the glossary corrections file')
parser.add_argument('Files', type=str, nargs='+', help='List of file paths to translate')
parser.add_argument('--SugoiDirectory', type=str, help='Path to the sugoi directory, required if Translator is \'Batch\' or \'Offline\'')
parser.add_argument('--BatchSize', type=int, help='Number of lines to translate at once, required if Translator is \'Batch\'')
parser.add_argument('--TimeoutWait', type=int, help='Number of seconds to wait before resuming translation after a timeout, required if Translator is \'Online\'')

args = parser.parse_args()

if args.Translator == 'Online' and args.TimeoutWait is None:
    parser.error('--TimeoutWait is required if Translator is \'Online\'')

if args.Translator == 'Offline' and args.SugoiDirectory is None:
    parser.error('--SugoiDirectory is required if Translator is \'Offline\'')

if args.Translator == 'Batch' and args.SugoiDirectory is None:
    parser.error('--SugoiDirectory is required if Translator is \'Batch\'')

if args.Translator == 'Batch' and args.BatchSize is None:
    parser.error('--BatchSize is required if Translator is \'Batch\'')

glossary = Glossary(args.GlossaryNames, args.GlossaryCorrections)
outputFormat = LineByLineFormat() if args.OutputFormat == 'LineByLine' else EnglishOnlyFormat()

translator = None
if args.Translator == 'Batch':
    translator = BatchTranslator(outputFormat, glossary, args.SugoiDirectory, args.BatchSize)
elif args.Translator == 'Online':
    translator = OnlineTranslator(outputFormat, glossary, args.TimeoutWait)
else:
    translator = OfflineTranslator(outputFormat, glossary, args.SugoiDirectory)

files = args.Files
for file in files:
    translator.translate(file)

translator.__del__()

