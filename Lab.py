from main import db
class Lab:
    def __init__(self, id, theme, deadline, maxScope,subject_id):
        self.id = id
        self.theme = theme
        self.dealine = deadline
        self.maxScope = maxScope
        self.subjectId = subject_id

    @staticmethod
    def map(object):
        newLab = Lab(object.id,object.theme,object.deadline,object.maxScope,object.subjectId)
        return newLab
    @staticmethod
    def getAllWithout(Id):
        session = db.Session()
        out = []
        q = session.query(Lab).filter(id != Id).all()
        for c in q:
            out.append(c)
        return out