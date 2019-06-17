"""
Usage: python table2brackets.py <tableFile.csv> <outputFile.txt>
"""

import sys

from markup.BracketsRenderer import BracketsRenderer
from markup.main import main
from markup.TableParser import TableParser


if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python xml2brackets.py <table.csv> <outputFile.txt>\n")
        exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    parser = TableParser()
    renderer = BracketsRenderer()

    main(parser, renderer, inputFile, outputFile)
