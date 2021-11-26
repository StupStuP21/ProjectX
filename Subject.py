import Labs
from sqlalchemy import  Integer, Column, VARCHAR
from main import Base,engine,session


class Subject(Base):
    __tablename__ = 'Subjects'
    __table_args__ = {'extend_existing': True}

    def __init__(self, Name):
        self.Name = Name

    Subject_ID = Column(Integer, nullable=False, primary_key=True, unique=True)
    Name = Column(VARCHAR(50), nullable=False)

    def getSubjectId(self):
        return self.Subject_ID
    def getName(self):
        return self.Name

    def getAllLabsForSubject(self):
        labs = session.query(Labs.Lab).filter(Labs.Lab.Subject_ID == self.Subject_ID).all()
        return labs

    @staticmethod
    def addNewStudentInBase(SubjectObject):
        session.add(SubjectObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Name):
        newSubject = Subject(Name)
        session.add(newSubject)
        session.commit()
        return newSubject

Base.metadata.create_all(engine)
