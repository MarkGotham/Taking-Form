import os

from markup.Annotation import Annotation
from markup.AnnotationGroup import AnnotationGroup
from markup.IParser import IParser
from markup.ParseError import ParseError
from music21 import bar
from music21 import common
from music21 import converter
from music21 import expressions

class MusicXmlParser(IParser):
    def __init__(self):
        self.__inputFile = None
        self.__annotations = None
        self.__finalMeasure = None
        self.__finalBeat = None

    def load(self, inputFile: str) -> None:
        if not os.path.isfile(inputFile):
            raise FileNotFoundError("Could not find "+inputFile+". File does not exist.")

        # test parse -- ignore result
        converter.parse(inputFile)      # TODO: better error handling here

        self.__inputFile = inputFile

    def parse(self):
        """
        :raises: # TODO better exception when no input file loaded
        :raises: # TODO exception for syntax error in annotation
        """
        if self.__inputFile is None:
            raise Exception("No input file loaded.")

        score = converter.parse(self.__inputFile)

        finalMeasure = 0
        finalBeat = 0
        annotationGroups = []

        finalMeasure = score.recurse().getElementsByClass('Measure')[-1].measureNumber

        testExpressions = [x for x in score.recurse().getElementsByClass('TextExpression') \
                            if Annotation.IsAnnotation(x.content)]

        for element in testExpressions:
            try:
                annotationGroups.append(AnnotationGroup(element.content, element.measureNumber, element.beat))
            except Exception as e:
                raise ParseError(element.content, finalMeasure)

        self.__annotations = [annotation for group in annotationGroups for annotation in group.getAnnotations()]
        self.__finalMeasure = finalMeasure
        self.__finalBeat = finalBeat

    def getAnnotations(self) -> [Annotation]:
        if self.__annotations is None:
            raise Exception("Call parse() first.")

        return self.__annotations

    def getScoreEnd(self) -> (int, int):
        """
        :return: Index of final measure and beat in score
        """

        if (self.__finalMeasure is None) or (self.__finalBeat is None):
            raise Exception("Call parse() first.")

        return (self.__finalMeasure, self.__finalBeat)
