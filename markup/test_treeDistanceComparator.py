import os
import sys
import traceback

from unittest import TestCase

from markup import ParseError
from Annotation import Annotation
from MusicXmlParser import MusicXmlParser
from Tree import Tree
from TreeDistanceComparator import TreeDistanceComparator


class TestTreeDistanceComparator(TestCase):

    def makeTrees(self, mxlPath1, mxlPath2):
        trees = []

        for inputFile in [mxlPath1, mxlPath2]:
            parser = MusicXmlParser()
            try:
                parser.load(inputFile)
            except:
                sys.stderr.write("Could not load " + inputFile + ". Exiting.\n")
                traceback.print_exc()  # TODO tidy
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

        self.assertEqual(2, len(trees))

        return trees


    def test_op2no1movt1_distanceToSelfIsZero(self):
        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        inFile = thisFilePath + "/../examples/op2no1movt1.mxl"

        trees = self.makeTrees(inFile, inFile)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1])
        treeDistanceComparator.compare()

        self.assertEqual(0, treeDistanceComparator.getTreeEditDistance())


    def test_op2no1movt1_costOfRemovingNodeAtLevel2IsGreaterThanRemovingNodeAtLevel6(self):
        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        inFile1 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_orig.mxl"
        inFile2 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_level6noderemoved.mxl"
        inFile3 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_level1noderemoved.mxl"

        trees = self.makeTrees(inFile1, inFile2)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1])
        treeDistanceComparator.compare()

        editDistanceRemovingLevel6Node = treeDistanceComparator.getTreeEditDistance()

        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        trees = self.makeTrees(inFile1, inFile3)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1])
        treeDistanceComparator.compare()

        editDistanceRemovingLevel1Node = treeDistanceComparator.getTreeEditDistance()

        print(str(editDistanceRemovingLevel1Node)+"\n")
        print(str(editDistanceRemovingLevel6Node)+"\n")

        self.assertGreater(editDistanceRemovingLevel1Node, editDistanceRemovingLevel6Node)


    def test_op2no1movt1_costOfInsertingAtLevel6IsSameAsRemovingAtLevel6(self):
        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        inFile1 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_orig.mxl"
        inFile2 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_level6noderemoved.mxl"
        inFile3 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_level6nodeadded.mxl"

        trees = self.makeTrees(inFile1, inFile2)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1])
        treeDistanceComparator.compare()

        editDistanceRemovingLevel6Node = treeDistanceComparator.getTreeEditDistance()

        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        trees = self.makeTrees(inFile1, inFile3)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1])
        treeDistanceComparator.compare()

        editDistanceAddingLevel6Node = treeDistanceComparator.getTreeEditDistance()

        print(editDistanceAddingLevel6Node)
        print(editDistanceRemovingLevel6Node)

        self.assertEqual(editDistanceAddingLevel6Node, editDistanceRemovingLevel6Node)

    def test_op2no1movt1_differencesAtLevel6AreIgnoredIfMaxDepthIsThree(self):
        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        inFile1 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_orig.mxl"
        inFile2 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_level6noderemoved.mxl"
        inFile3 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_level6nodeadded.mxl"

        trees = self.makeTrees(inFile1, inFile2)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1], maxComparisonDepth=3)
        treeDistanceComparator.compare()

        editDistanceRemovingLevel6Node = treeDistanceComparator.getTreeEditDistance()

        self.assertEqual(0, editDistanceRemovingLevel6Node)

        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        trees = self.makeTrees(inFile1, inFile3)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1], maxComparisonDepth=3)
        treeDistanceComparator.compare()

        editDistanceAddingLevel6Node = treeDistanceComparator.getTreeEditDistance()

        self.assertEqual(0, editDistanceAddingLevel6Node)

    def test_op2no1movt1_differencesAtLevel1AreNotIgnoredIfMaxDepthIsThree(self):
        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        inFile1 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_orig.mxl"
        inFile2 = thisFilePath + "/../examples/op2no1movt1_treetests/op2no1movt1_level1noderemoved.mxl"

        trees = self.makeTrees(inFile1, inFile2)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1])
        treeDistanceComparator.compare()

        editDistanceWithNoMaxDepth = treeDistanceComparator.getTreeEditDistance()

        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        trees = self.makeTrees(inFile1, inFile2)

        treeDistanceComparator = TreeDistanceComparator(trees[0], trees[1], maxComparisonDepth=3)
        treeDistanceComparator.compare()

        editDistanceWithMaxDepth = treeDistanceComparator.getTreeEditDistance()

        print(editDistanceWithMaxDepth)
        print(editDistanceWithNoMaxDepth)

        self.assertEqual(editDistanceWithNoMaxDepth, editDistanceWithMaxDepth)
