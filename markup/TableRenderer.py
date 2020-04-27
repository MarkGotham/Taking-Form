import numpy as np

from IRenderer import IRenderer
from Tree import Tree


HEADER_ROWS = 1
HEADER_COLUMNS = 2

class TableRenderer(IRenderer):
    def __init__(self):
        self.__tree = None
        self.__outputFile = None
        self.__array = None

    def renderToFile(self, tree : Tree, outputFile : str) -> None:
        self.__tree = tree
        self.__outputFile = outputFile

        self.__createEmptyArray()
        self.__initialiseHeaderRows()
        self.__treeToArray(self.__tree.root)
        self.__writeToOutputFile()

    def __createEmptyArray(self):
        numRows = self.__tree.getTotalMeasures() + HEADER_ROWS
        numColumns = self.__tree.getMaxDepth() + HEADER_COLUMNS

        self.__array = np.empty([numRows, numColumns], dtype=object)

        for i in range(numRows):
            for j in range(numColumns):
                self.__array[i,j] = ""

    def __initialiseHeaderRows(self):
        self.__array[0,0] = "Measure"
        self.__array[0,1] = "Beat"
        self.__array[0,2] = "Form and Phrase"

        for measure in range(1, self.__tree.getTotalMeasures()+1):
            self.__array[measure, 0] = str(measure)
            self.__array[measure, 1] = "1"

    def __treeToArray(self, node):
        if node.getDepth() > 0:
            self.__array[node.getMeasure() + HEADER_ROWS - 1, node.getDepth() + HEADER_COLUMNS - 1] = node.getId()
            self.__array[node.getMeasure() + HEADER_ROWS - 1, 1] = node.getBeat()

        for child in node.children:
            self.__treeToArray(child)

    def __writeToOutputFile(self, separator=','):
        numRows, numColumns = self.__array.shape

        with open(self.__outputFile, 'w') as file:
            for row in range(numRows):
                for column in range(numColumns):
                    if column>0:
                        file.write(separator)
                    file.write(str(self.__array[row,column]))
                file.write("\n")
