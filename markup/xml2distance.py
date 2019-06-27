"""
Usage: python xml2distance.py <source1.musicxml> <source2.musicxml>
Output: A number (the tree edit distance between the two sources) and a string indicating the tree edits required.
"""

import sys
import traceback

from markup.ParseError import ParseError
from markup.MusicXmlParser import MusicXmlParser
from markup.Tree import Tree
from markup.TreeDistanceComparator import TreeDistanceComparator


if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python xml2distance.py <source1.musicxml> <source2.musicxml>\n")
        exit(1)

    inputFiles = [sys.argv[1], sys.argv[2]]
    trees = []

    for inputFile in inputFiles:
        parser = MusicXmlParser()
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
        trees.append(tree)

    assert(len(trees) == 2)

    treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1])
    treeDistanceComparator.compare()

    distance = treeDistanceComparator.getTreeEditDistance()
    print(str(distance))

