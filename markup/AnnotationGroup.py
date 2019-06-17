from markup.Annotation import Annotation


class AnnotationGroup:
    def __init__(self, text : str, measure : int, beat : int):
        self.__text = text
        self.__measure = measure
        self.__beat = int(round(beat))

    def getAnnotations(self) -> [Annotation]:
        self.__text = self.__text.replace(", ", ",")
        annotations = [Annotation(text, self.__measure, self.__beat) for text in self.__text.split(",")]
        return annotations
