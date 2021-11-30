import Labs
from sqlalchemy import Integer, Column, VARCHAR
from DatabaseConnect import connect


class Subject(connect.Base):
    __tablename__ = 'Subjects'
    __table_args__ = {'extend_existing': True}

    def __init__(self, Name):
        self.Name = Name

    Subject_ID = Column(Integer, nullable=False, primary_key=True, unique=True)
    Name = Column(VARCHAR(255), nullable=False)

    def getSubjectId(self):
        return self.Subject_ID

    def getName(self):
        return self.Name

    def getAllLabsForSubject(self):
        labs = connect.session.query(Labs.Lab).filter(Labs.Lab.Subject_ID == self.Subject_ID).all()
        return labs

    @staticmethod
    def addNewInBase(SubjectObject):
        connect.session.add(SubjectObject)
        connect.session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Name):
        newSubject = Subject(Name)
        connect.session.add(newSubject)
        connect.session.commit()
        return newSubject


connect.Base.metadata.create_all(connect.engine)
