from IRenderer import IRenderer
from Tree import Tree


INDENT_SIZE = 4             # number of spaces added for each level in the tree
PRINT_BAR_NUMBERS = False   # TODO add bar numbers so we can go back and forth between tabular and bracket notation


class BracketsRenderer(IRenderer):
    def __init__(self):
        self.__tree = None
        self.__outputFile = None
        self.__fileHandle = None

    def renderToFile(self, tree : Tree, outputFile : str) -> None:
        self.__tree = tree
        self.__outputFile = outputFile

        with open(self.__outputFile, 'w') as self.__fileHandle:
            self.__renderNode(self.__tree.root)

    def __renderNode(self, node):
        indent = INDENT_SIZE * (node.getDepth()-1) * ' '

        if node.getDepth() > 0:
            self.__fileHandle.write(indent)
            self.__fileHandle.write("[")
            self.__fileHandle.write(node.getId())
            self.__fileHandle.write("\n")

        childIndex = 0
        while childIndex < len(node.children):
            if node.children[childIndex].isLeaf():
                childId = node.children[childIndex].getId()
                self.__fileHandle.write(indent)
                self.__fileHandle.write(' '*INDENT_SIZE)
                self.__fileHandle.write("[")
                self.__fileHandle.write(childId)
                while (childIndex < len(node.children) and
                        node.children[childIndex].getId() == childId and
                        node.children[childIndex].isLeaf()):
                    self.__fileHandle.write(' ')
                    self.__fileHandle.write(str(node.children[childIndex].span))
                    childIndex = childIndex + 1
                self.__fileHandle.write("]")
                self.__fileHandle.write("\n")
            else:
                self.__renderNode(node.children[childIndex])
                childIndex = childIndex + 1

        if node.getDepth() > 0:
            self.__fileHandle.write(indent)
            self.__fileHandle.write("]")
            self.__fileHandle.write("\n")
