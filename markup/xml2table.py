"""
Usage: python xml2table.py <source.musicxml> <outputFile.csv>
"""

import sys

from markup.MusicXmlParser import MusicXmlParser
from markup.main import main
from markup.TableRenderer import TableRenderer


if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python xml2table.py <source.musicxml> <outputFile.csv>\n")
        exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    parser = MusicXmlParser()
    renderer = TableRenderer()

    main(parser, renderer, inputFile, outputFile)
