from unittest import TestCase

from markup.Annotation import Annotation
from markup.Tree import Tree


class TestTree(TestCase):
    def test_check(self):
        self.fail()

    def test_build(self):
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

        # parameter totalMeasure is arbitrary -- use to test leaf distances
        tree.build(annotations, 19)

        tree.print()

        # TODO complete
        #self.fail()

    def test_spanCalculation(self):
        self.fail()
