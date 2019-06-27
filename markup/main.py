"""
Converter code used by xml2table.py, xml2brackets.py, table2brackets.py
"""

import sys
import traceback

from markup.IParser import IParser
from markup.IRenderer import IRenderer
from markup.ParseError import ParseError
from markup.Tree import Tree


def main(parser : IParser, renderer : IRenderer, inputFile : str, outputFile : str) -> None:
    try:
        parser.load(inputFile)
    except:
        sys.stderr.write("Could not load "+inputFile+". Exiting.\n")
        traceback.print_exc()    # TODO tidy
        exit(1)

    try:
        parser.parse()
    except ParseError as e:
        print(e)
        sys.stderr.write("Found badly formed annotation. Exiting.\n")
        exit(1)

    tree = Tree()
    tree.build(parser.getAnnotations(), parser.getScoreEnd()[0])

    try:
        renderer.renderToFile(tree, outputFile)
    except:
        sys.stderr.write("Could not render to "+outputFile+". Exiting.\n")
        exit(1)
