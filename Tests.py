from sqlalchemy import Integer, Column, ForeignKey,REAL
from sqlalchemy.orm import relationship

import Students
from main import db
from Subject import Subject
from Tasks import Task


class Test(db.Base):
    __tablename__ = 'Tests'
    __table_args__ = {'extend_existing': True}

    def __init__(self, test_Id,MaxTScore, Subject_ID):
        self.Test_ID = test_Id
        self.Subject_ID = Subject_ID
        self.MaxTScore = MaxTScore

    Test_ID = Column(Integer, nullable=False, primary_key=True, unique=True)
    MaxTScore = Column(REAL, nullable=False)
    Subject_ID = Column(Integer, ForeignKey('Subjects.Subject_ID'))
    Subject = relationship(Subject)

    @staticmethod
    def addNewInBase(TestObject):
        session = db.Session()
        session.add(TestObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(MaxTScore, Subject_ID):
        session = db.Session()
        newTest = Test(MaxTScore, Subject_ID)
        session.add(newTest)
        session.commit()
        return newTest

    @staticmethod
    def getTestById(id):
        tests = db.getAllTests()
        for i in tests:
            if i[0]==id:
                newTest = Test(i[0],i[1],i[2])
                break
        return newTest

    @staticmethod
    def getListOfAllTasksInTestIds(testId):
        complTasks = db.getAllTestTaskStud()
        currentTasks = []
        for i in complTasks:
            if i.Test_Id == testId:
                currentStudentId = i.Stud_Id
                break
        listOfTasks = []
        for i in complTasks:
            if i.Test_Id==testId and i.Stud_Id==currentStudentId:
                listOfTasks.append(i.Task_Id)
        return listOfTasks

db.Base.metadata.create_all(db.engine)
