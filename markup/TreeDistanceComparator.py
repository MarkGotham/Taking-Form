
import zss

class TreeDistanceComparator:
    def __init__(self, tree1, tree2, maxComparisonDepth=None):
        self.__tree1 = tree1.root
        self.__tree2 = tree2.root
        self.__treeHeight = max(tree1.getMaxDepth(), tree2.getMaxDepth())
        self.__maxDepth = maxComparisonDepth
        self.__treeEditDistance = None
        self.__treeEditOperations = None

    def __defaultComparator(self, node1, node2):
        if node1 == '' and node2 != '':
            # insert cost
            return 1 + self.__treeHeight - node2[1]

        if node1 != '' and node2 == '':
            # remove cost
            return 1 + self.__treeHeight - node1[1]

        # update cost

        node1label = node1[0]
        node2label = node2[0]

        node1depth = node1[1]
        node2depth = node2[1]

        differenceInDepth = max(node1depth, node2depth) - min(node1depth, node2depth)

        if (node1label == node2label) and (differenceInDepth == 0):
            # node is same -- no cost to update
            return 0
        elif (node1label == 'X' or node2label == 'X') and (differenceInDepth == 0):
            # small cost to turn any node into an "X"
            return 1
        elif node1label == 'X' or node2label == 'X':
            return 1+2*differenceInDepth
        else:
            return 2+2*differenceInDepth

    def __getLabel(self, node):
        if node.__class__.__name__ == "RootNode":
            return ["Root", 0]

        return [node.getId(), node.getDepth()]

    def __getChildren(self, node):
        if (self.__maxDepth is not None) and (node.getDepth() >= self.__maxDepth):
            return []

        return node.children

    def compare(self, comparator=None):
        if comparator is None:
            comparator = self.__defaultComparator

        self.__treeEditDistance, self.__treeEditOperations = zss.simple_distance(
            self.__tree1, self.__tree2, self.__getChildren, self.__getLabel, comparator, return_operations=True
        )

    def getTreeEditDistance(self):
        if self.__treeEditDistance is None:
            self.compare()
        return self.__treeEditDistance

    def getTreeEditOperations(self):
        if self.__treeEditOperations is None:
            self.compare()
        return self.__treeEditOperations
