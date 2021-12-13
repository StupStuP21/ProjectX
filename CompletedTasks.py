from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from main import db
from Students import Student
from Tests import Test
from Tasks import Task

class CompletedTask(db.Base):
    __tablename__ = 'TestTaskStud'
    __table_args__ = {'extend_existing': True}

    def __init__(self, Stud_ID, Test_ID, Task_ID, GetTScore):
        self.Stud_Id = Stud_ID
        self.Test_Id = Test_ID
        self.Task_Id = Task_ID
        self.GetTaskScore = GetTScore

    Stud_Id = Column(Integer, ForeignKey('Students.Student_Id'), primary_key=True, unique=True)
    Test_Id = Column(Integer, ForeignKey('Tests.Test_ID'), primary_key=True, unique=True)
    Task_Id = Column(Integer, ForeignKey('Tasks.Task_Id'), primary_key=True, unique=True)
    GetTaskScore = Column(Integer, nullable=True)
    Students = relationship(Student)
    Tests = relationship(Test)
    Tasks = relationship(Task)

    def Print(self):
        print("Student_Id:",self.Stud_Id,";","Test_Id:",self.Test_Id,";","Task_Id",self.Task_Id,";","GetTScore:",self.GetTaskScore)

    @staticmethod
    def addNewInBase(CompletedTaskObject):
        session = db.Session()
        session.add(CompletedTaskObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Stud_ID, Test_ID, Task_ID, GetTScore):
        session = db.Session()
        newCompletedTask = CompletedTask(Stud_ID, Test_ID, Task_ID, GetTScore)
        session.add(newCompletedTask)
        session.commit()
        return newCompletedTask

    @staticmethod
    def getAllCompletedTasksInTest(StudentObject,testId):
        completedTasksAll = db.getAllTestTaskStud()
        completedTasks = []
        for i in completedTasksAll:
            if i[0] == StudentObject.Student_Id and i[1] == testId:
                newTask = CompletedTask(i[0], i[1], i[2], i[3])
                completedTasks.append(newTask)
        return completedTasks

db.Base.metadata.create_all(db.engine)

