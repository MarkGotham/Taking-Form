from abc import ABCMeta, abstractmethod
from Tree import Tree


class IRenderer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def renderToFile(self, tree : Tree, outputFile : str) -> None:
        raise NotImplementedError()
