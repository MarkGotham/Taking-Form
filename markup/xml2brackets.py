"""
Usage: python xml2brackets.py <source.musicxml> <outputFile.txt>
"""

import sys

from markup.BracketsRenderer import BracketsRenderer
from markup.main import main
from markup.MusicXmlParser import MusicXmlParser


if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python xml2brackets.py <source.musicxml> <outputFile.txt>\n")
        exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    parser = MusicXmlParser()
    renderer = BracketsRenderer()

    main(parser, renderer, inputFile, outputFile)
