import math

#import Students
#import Labs

nNearest = 5
class Filterisation:
    currentStudentId = ...

    students = [...]  # массив студентов
    labs = [...]  # массив лаб
    rates = [...]
    balls = dict()  # без сравнимого студента
    #currentStudentRates = dict()  # то же, что и balls, только для сравнимого студента

    def __init__(self,id):
        self.currentStudentId=id


    def getBalls(self):
        studId = ...
        labId = ...
        rate = ...
        if not studId in self.balls: #and studId != self.currentStudentId:
            self.balls[studId] = dict()
        self.balls[studId][labId] = rate

    def cosMetric(self, x, y):
        def dotLab(x, y):
            dist = 0.0
            for k in x:
                if k in y:
                    dist += x[k] * y[k]
            return dist

        return dotLab(x, y) / math.sqrt(dotLab(x, x)) / math.sqrt(dotLab(y, y))

    def getNearestStudents(self):
        studentsDistanced = [(x, self.cosMetric(self.balls(self.currentStudentId),self.balls(x))) for x in self.balls if x != self.currentStudentId]
        nBestStudentsDistanced = sorted(studentsDistanced,reverse=True)[:nNearest]
        return nBestStudentsDistanced