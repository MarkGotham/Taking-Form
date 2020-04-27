import numpy as np
import os

from Annotation import Annotation
from IParser import IParser
from TableAnnotation import TableAnnotation


class TableParser(IParser):
    def __init__(self):
        self.__inputFile = None
        self.__annotations = None
        self.__finalMeasure = None
        self.__finalBeat = None

    def load(self, inputFile: str) -> None:
        if not os.path.isfile(inputFile):
            raise FileNotFoundError("Could not find "+inputFile+". File does not exist.")

        # test parse -- ignore result
        np.genfromtxt(inputFile, delimiter=',')

        self.__inputFile = inputFile

    def parse(self):
        """
        :raises: # TODO better exception when no input file loaded
        :raises: # TODO exception for syntax error in annotation
        """
        if self.__inputFile is None:
            raise Exception("No input file loaded.")

        annotations = []
        array = np.genfromtxt(self.__inputFile, delimiter=',', dtype='object', skip_header=1).astype(str)
        numRows, numColumns = array.shape

        finalMeasure = 0
        finalBeat = 0

        for row in range(numRows):
            for column in range(2, numColumns):
                id = str(array[row][column])
                if len(id) > 0:
                    print(str(id) + ", " + str(array[row][0]) + ", " + str(array[row][1]))
                    annotations.append(TableAnnotation(str(id), column-1, int(array[row][0]), int(array[row][1])))

            if len(str(array[row][0])) > 0:
                finalMeasure = int(str(array[row][0]))
                finalBeat = int(str(array[row][1]))

        self.__annotations = annotations
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
