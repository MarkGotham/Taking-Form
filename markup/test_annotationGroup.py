from unittest import TestCase

from Annotation import Annotation
from AnnotationGroup import AnnotationGroup

class TestAnnotationGroup(TestCase):
    def test_getAnnotations_SingleAnnotation_CorrectString(self):
        grp = AnnotationGroup("6: Basic idea", 1, 1)
        self.assertEqual(
            [Annotation("6: Basic idea", 1, 1)],
            grp.getAnnotations()
        )

    def test_getAnnotations_ManyAnnotations_CorrectString_SpaceAfterComma(self):
        grp = AnnotationGroup("1: Exposition, 2: First Subject Group, 3: Theme a, 4: Sentence, 5: Presentation, 6: Basic idea", 1, 1)
        self.assertEqual(
            [
                Annotation("1: Exposition", 1, 1),
                Annotation("2: First Subject Group", 1, 1),
                Annotation("3: Theme a", 1, 1),
                Annotation("4: Sentence", 1, 1),
                Annotation("5: Presentation", 1, 1),
                Annotation("6: Basic idea", 1, 1),
            ],
            grp.getAnnotations()
        )

    def test_getAnnotations_ManyAnnotations_CorrectString_NoSpaceAfterComma(self):
        grp = AnnotationGroup("1: Exposition,2: First Subject Group,3: Theme a,4: Sentence,5: Presentation,6: Basic idea", 1, 1)
        self.assertEqual(
            [
                Annotation("1: Exposition", 1, 1),
                Annotation("2: First Subject Group", 1, 1),
                Annotation("3: Theme a", 1, 1),
                Annotation("4: Sentence", 1, 1),
                Annotation("5: Presentation", 1, 1),
                Annotation("6: Basic idea", 1, 1),
            ],
            grp.getAnnotations()
        )

# todo: tests for measure & beat number
# todo: test exception for measure/beat number zero
