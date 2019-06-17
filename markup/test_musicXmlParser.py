import os

from unittest import TestCase

from markup.Annotation import Annotation
from markup.MusicXmlParser import MusicXmlParser

class TestMusicXmlParser(TestCase):
    def test_load(self):
        self.fail()

    def test_parse_Beethoven_SonateNo1(self):
        parser = MusicXmlParser()

        thisFilePath = os.path.dirname(os.path.abspath(__file__))
        parser.load(thisFilePath+"/../examples/op2no1movt1.musicxml")
        parser.parse()

        annotations = parser.getAnnotations()[:9]

        self.assertEqual(
            [Annotation("1: Exposition", 1, 4),
             Annotation("2: First Subject Group", 1, 4),
             Annotation("3: Theme a", 1, 4),
             Annotation("4: Sentence", 1, 4),
             Annotation("5: Presentation", 1, 4),
             Annotation("6: Basic idea", 1, 4),
             Annotation("6: Basic idea", 4, 1),
             Annotation("5: Continuation", 6, 1),
             Annotation("6: Fragmentation", 6, 1),
             ],
            annotations
        )

# todo: add remaining AnnotationGroups to SonateNo1
# todo: test load throws exception for file that doesn't exist
# todo: test load throws exception for invalid file
