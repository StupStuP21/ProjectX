from sqlalchemy import Integer, Column, ForeignKey,Date
from sqlalchemy.orm import relationship
from main import db
from Students import Student
from Tests import Test

class CompletedTest(db.Base):
    __tablename__ = 'TestStud'
    __table_args__ = {'extend_existing': True}

    def __init__(self, Stud_ID, Test_ID,GetTScore):
        self.Stud_Id=Stud_ID
        self.Test_Id=Test_ID
        self.GetTScore = GetTScore

    Stud_Id = Column(Integer,ForeignKey('Students.Student_Id'),primary_key=True,unique=True)
    Test_Id = Column(Integer,ForeignKey('Tests.Test_ID'),primary_key=True,unique=True)
    GetTScore = Column(Integer,nullable=False)
    Students = relationship(Student)
    Tests = relationship(Test)

    @staticmethod
    def addNewInBase(CompletedTestObject):
        session = db.Session()
        session.add(CompletedTestObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Stud_ID, Test_ID, GetTScore):
        session = db.Session()
        newCompletedTest = CompletedTest(Stud_ID, Test_ID, GetTScore)
        session.add(newCompletedTest)
        session.commit()
        return newCompletedTest




db.Base.metadata.create_all(db.engine)
