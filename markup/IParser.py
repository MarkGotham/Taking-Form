from abc import ABCMeta, abstractmethod

from markup.Annotation import Annotation


class IParser:
    __metaclass__ = ABCMeta

    @abstractmethod
    def load(self, inputFile : str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def parse(self):
        raise NotImplementedError()

    @abstractmethod
    def getAnnotations(self) -> [Annotation]:
        raise NotImplementedError()

    @abstractmethod
    def getScoreEnd(self) -> (int, int):
        raise NotImplementedError()
