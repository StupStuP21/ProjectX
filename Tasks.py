from sqlalchemy import Integer, Column, VARCHAR
from main import db


class Task(db.Base):
    __tablename__ = 'Tasks'
    __table_args__ = {'extend_existing': True}

    def __init__(self, Task_Id, Theme, Difficulty,MaxTScore):
        self.Task_Id = Task_Id
        self.Theme = Theme
        self.Difficulty = Difficulty
        self.MaxTScore = MaxTScore

    Task_Id = Column(Integer, nullable=False, primary_key=True, unique=True)
    Theme = Column(VARCHAR(255), nullable=False)
    Difficulty = Column(Integer, nullable=False)
    MaxTScore = Column(Integer, nullable=True)

    def Print(self):
        print("Task_Id:", self.Task_Id, ";", "Theme:", self.Theme, ";", "Difficulty:", self.Difficulty,";","MaxTScore:",self.MaxTScore)

    @staticmethod
    def addNewInBase(TaskObject):
        session = db.Session()
        session.add(TaskObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Theme, Difficulty):
        session = db.Session()
        newTask = Task(Theme, Difficulty)
        session.add(newTask)
        session.commit()
        return newTask

    @staticmethod
    def getAllTasksInTestByTaskId(listOfTasksId):
        AllTasks = db.getAllTasks()
        AllTasksInTest = []
        for i in AllTasks:
            if i[0] in listOfTasksId:
                newTask = Task(i[0], i[1], i[2],i[3])
                AllTasksInTest.append(newTask)
        return AllTasksInTest

    @staticmethod
    def getTasksById(Task_Id):
        AllTasks = db.getAllTasks()
        for i in AllTasks:
            if i[0] == Task_Id:
                currentTask = Task(i[0], i[1], i[2],i[3])
        return currentTask


db.Base.metadata.create_all(db.engine)
