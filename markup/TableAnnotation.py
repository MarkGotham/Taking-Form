from Annotation import Annotation

class TableAnnotation(Annotation):
    def __init__(self, id : str, depth : int, measure : int, beat : int):
        super().__init__(str(depth)+": "+id, measure, beat)
