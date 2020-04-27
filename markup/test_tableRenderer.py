import os

from Annotation import Annotation
from TableRenderer import TableRenderer
from Tree import Tree
from unittest import TestCase


class TestTableRenderer(TestCase):
    def test_renderToFile(self):
        annotations = [
            Annotation("1: Exposition", 1, 4),
            Annotation("2: First Subject Group", 1, 4),
            Annotation("3: Theme a", 1, 4),
            Annotation("4: Sentence", 1, 4),
            Annotation("5: Presentation", 1, 4),
            Annotation("6: Basic idea", 1, 4),
            Annotation("6: Basic idea", 4, 1),
            Annotation("5: Continuation", 6, 1),
            Annotation("6: Fragmentation", 6, 1),
            Annotation("6: Cadence", 8, 1),
            Annotation("2: Transition", 10, 1),
            Annotation("3: Theme a", 10, 1),
        ]

        tree = Tree()

        tree.build(annotations, 19)

        renderer = TableRenderer()
        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        renderer.renderToFile(tree, thisFilePath + "/test.csv")


        self.fail()
