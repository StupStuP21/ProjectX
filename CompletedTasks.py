from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from DatabaseConnect import connect
from Students import Student
from Tests import Test
from Tasks import Task


class CompletedTask(connect.Base):
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

    @staticmethod
    def addNewInBase(CompletedTaskObject):
        connect.session.add(CompletedTaskObject)
        connect.session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Stud_ID, Test_ID, Task_ID, GetTScore):
        newCompletedTask = CompletedTask(Stud_ID, Test_ID, Task_ID, GetTScore)
        connect.session.add(newCompletedTask)
        connect.session.commit()
        return newCompletedTask


connect.Base.metadata.create_all(connect.engine)

