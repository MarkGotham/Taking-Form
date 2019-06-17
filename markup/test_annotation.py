from unittest import TestCase

from markup.Annotation import Annotation


class TestAnnotation(TestCase):
    def test_IsAnnotation_TruePositive(self):
        self.assertTrue(Annotation.IsAnnotation(
            "1: Exposition, 2: First Subject Group, 3: Theme a, 4: Sentence, 5: Presentation, 6: Basic idea"))
        self.assertTrue(Annotation.IsAnnotation(
            "6: Basic idea"))
        self.assertTrue(Annotation.IsAnnotation(
            "5: Continuation, 6: Fragmentation"))
        self.assertTrue(Annotation.IsAnnotation(
            "6: Cadence"))
        self.assertTrue(Annotation.IsAnnotation(
            "2: Transition, 3: Theme a"))
        self.assertTrue(Annotation.IsAnnotation(
            "4: X"))
        self.assertTrue(Annotation.IsAnnotation(
            "401: X, 502: X"))
        self.assertTrue(Annotation.IsAnnotation(
            "20: Second Subject Group, 3: Theme b, 4: Sentence, 5: Presentation, 6: Basic idea"))


    def test_IsAnnotation_TrueNegative(self):
        self.assertFalse(Annotation.IsAnnotation(
            "Allegro"))
        self.assertFalse(Annotation.IsAnnotation(
            "Ludwig van Beethoven"))
        self.assertFalse(Annotation.IsAnnotation(
            "1 A Test"))
        self.assertFalse(Annotation.IsAnnotation(
            "A: A Test"))

    def test_depth(self):
        self.assertEqual(
            1,
            Annotation("1: Exposition", 1, 4).depth
        )
        self.assertEqual(
            2,
            Annotation("2: First Subject Group", 1, 4).depth
        )
        self.assertEqual(
            3,
            Annotation("3: Theme a", 1, 4).depth
        )
        self.assertEqual(
            4,
            Annotation("4: Sentence", 1, 4).depth
        )
        self.assertEqual(
            5,
            Annotation("5: Presentation", 1, 4).depth
        )
        self.assertEqual(
            6,
            Annotation("6: Basic idea", 1, 4).depth
        )
        self.assertEqual(
            5,
            Annotation("5: Continuation", 6, 1).depth
        )
        self.assertEqual(
            6,
            Annotation("6: Fragmentation", 6, 1).depth
        )

    def test_id(self):
        self.assertEqual(
            "Exposition",
            Annotation("1:Exposition", 1, 4).id
        )
        self.assertEqual(
            "Exposition",
            Annotation("1: Exposition", 1, 4).id
        )
        self.assertEqual(
            "First Subject Group",
            Annotation("2:First Subject Group", 1, 4).id
        )
        self.assertEqual(
            "First Subject Group",
            Annotation("2: First Subject Group", 1, 4).id
        )
        self.assertEqual(
            "Theme a",
            Annotation("3:Theme a", 1, 4).id
        )
        self.assertEqual(
            "Theme a",
            Annotation("3: Theme a", 1, 4).id
        )
        self.assertEqual(
            "Sentence",
            Annotation("4:Sentence", 1, 4).id
        )
        self.assertEqual(
            "Sentence",
            Annotation("4: Sentence", 1, 4).id
        )
        self.assertEqual(
            "Presentation",
            Annotation("5:Presentation", 1, 4).id
        )
        self.assertEqual(
            "Presentation",
            Annotation("5: Presentation", 1, 4).id
        )
        self.assertEqual(
            "Basic idea",
            Annotation("6:Basic idea", 1, 4).id
        )
        self.assertEqual(
            "Basic idea",
            Annotation("6: Basic idea", 1, 4).id
        )
        self.assertEqual(
            "Continuation",
            Annotation("5:Continuation", 6, 1).id
        )
        self.assertEqual(
            "Continuation",
            Annotation("5: Continuation", 6, 1).id
        )
        self.assertEqual(
            "Fragmentation",
            Annotation("6:Fragmentation", 6, 1).id
        )
        self.assertEqual(
            "Fragmentation",
            Annotation("6: Fragmentation", 6, 1).id
        )
