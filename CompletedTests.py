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

    @staticmethod
    def getAllByTestId(testId):
        allTests = db.getAllTestStud()
        allTestsById = []
        for i in allTests:
            if (i[1]==testId):
                newCompletedTest = CompletedTest(i[0],i[1],i[2])
                allTestsById.append(newCompletedTest)
        return allTestsById

    @staticmethod
    def getAllStudentsWithCompletedTest(testId):
        students = db.getAllStudents()
        sstudents = []
        completedTests = CompletedTest.getAllByTestId(testId)
        for i in students:
            for x in completedTests:
                if (i[0] == x.Stud_Id):
                    newStudent = Student(i[0], i[1], i[2], i[3])
                    sstudents.append(newStudent)
                    break
        return sstudents

    @staticmethod
    def getCompletedTestByStudIdAndTestId(studentObject,testObject):
        tests = db.getAllTestStud()
        for i in tests:
            if (i[0] == studentObject.Student_Id and i[1]==testObject.Test_ID):
                newCompletedTest = CompletedTest(i[0],i[1],i[2])
        return newCompletedTest



db.Base.metadata.create_all(db.engine)
