import re

from ParseError import ParseError

class Annotation:
    def __init__(self, text : str, measure : int, beat : float):
        self.measure = measure
        self.beat = beat

        text = text.replace("$", "")

        match = re.search('([0-9]+):\s?([^~]+)~?(.*)', text)

        if match is None:
            raise ParseError(text, measure)

        matchGroups = match.groups(0)

        self.depth = int(matchGroups[0])
        self.id = matchGroups[1]
        self.comment = matchGroups[2]

    @staticmethod
    def IsAnnotation(text : str) -> bool:
        pattern = re.compile("[0-9]+:")

        # docs on re.match: If zero or more characters at the beginning of the string match
        # the regular expression pattern (i.e. implied "^" at start of regex)
        return pattern.match(text)

    def __repr__(self):
        return f'{self.id}({self.measure},{round(self.beat, 2)})'

    def __eq__(self, other):
        if isinstance(other, Annotation):
            return self.measure == other.measure and self.beat == other.beat and self.id == other.id
        return False
