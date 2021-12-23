class testModel:
    def __init__(self, tup):
        self.id = tup[0]
        self.MaxTScore = tup[1]
        self.subjectId = tup[2]
        self.Name = tup[3]
    def __str__(self):
        return str(self.id)
    def __repr__(self):
        return str(self.id)
