
# TODO tidy
class ParseError(Exception):
    def __init__(self, annotationContent, bar):
        self.annotationContent = annotationContent
        self.bar = bar

    def __str__(self):
        return "Parse error | Bar " + str(self.bar) + " | " + self.annotationContent

    def __repr__(self):
        return self.__str__()

