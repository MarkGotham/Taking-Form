from markup.Annotation import Annotation

import sys

class TreeBuildException(Exception):
    def __init__(self, annotation):
        self.annotation = annotation

class Node:
    def __init__(self, annotation : Annotation = None):
        self.annotation = annotation
        self.span = None
        self.children = []

    def getDepth(self) -> int:
        return self.annotation.depth

    def getMeasure(self) -> int:
        return self.annotation.measure

    def getBeat(self) -> int:
        return self.annotation.beat

    def getId(self) -> str:
        return self.annotation.id

    def addChild(self, annotation):
        if (annotation.depth == self.getDepth()+1):
            self.children.append(Node(annotation))
        else:
            if (len(self.children) > 0):
                self.children[-1].addChild(annotation)
            else:
                if (annotation.depth - self.getDepth() == 1):
                    self.children = [Node(annotation)]
                else: # TODO HACK need to think about how to correctly handle this case   #raise TreeBuildException(annotation)
                    self.children = [Node(Annotation(str(self.getDepth()+1)+": FAKE LABEL", annotation.measure, annotation.beat))]
                    self.addChild(annotation)

    def getNextNode(self, nodeBefore):
        """
        In depth-first traversal of tree, get first leaf node with measure number higher than nodeBefore
        :return: None for last node in tree
        """
        if (self.getDepth() <= nodeBefore.getDepth()) and (self.getMeasure() > nodeBefore.getMeasure()):
            return self

        for child in self.children:
            nextNode = child.getNextNode(nodeBefore)
            if nextNode is not None:
                return nextNode

        return None

    def isLeaf(self) -> bool:
        return len(self.children) == 0

    def calculateSpanLengths(self, root):
        nextNode = root.getNextNode(self)

        if nextNode is not None:
            self.span = nextNode.getMeasure() - self.getMeasure()
        else:
            self.span = root.getTotalMeasures() - self.getMeasure() + 1

        for child in self.children:
            child.calculateSpanLengths(root)

    def print(self):
        indent = " "*2*self.getDepth()

        sys.stdout.write(indent + self.annotation.id + "(" + str(self.annotation.measure) + "," + str(
            self.annotation.beat) + ")")
        sys.stdout.write("[" + str(self.span) + "]")
        sys.stdout.write("\n")

        for child in self.children:
            child.print()

class RootNode(Node):
    def __init__(self, totalMeasures):
        super().__init__()
        self.__totalMeasures = totalMeasures

    def getDepth(self) -> int:
        return 0

    def getTotalMeasures(self) -> int:
        return self.__totalMeasures

    def getMeasure(self) -> int:
        return 1

    def calculateSpanLengths(self, root):
        super().calculateSpanLengths(self)

    def print(self):
        sys.stdout.write("Root\n")
        for child in self.children:
            child.print()

class Tree:
    def __init__(self):
        self.root = None
        self.__maxDepth = None

    def check(self):
        # TODO: check levels are continuous etc.
        pass

    def build(self, annotations : [Annotation], totalMeasures):
        self.root = RootNode(totalMeasures)

        self.__maxDepth = 0
        for annotation in annotations:
            self.root.addChild(annotation)
            self.__maxDepth = max(self.__maxDepth, annotation.depth)

        self.root.calculateSpanLengths(self.root)

    def getTotalMeasures(self) -> int:
        return self.root.getTotalMeasures()

    def getMaxDepth(self):
        return self.__maxDepth

    def print(self):
        self.root.print()
