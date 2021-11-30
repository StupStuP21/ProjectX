from sqlalchemy import Integer, Column, VARCHAR
from DatabaseConnect import connect

class Task(connect.Base):
    __tablename__ = 'Tasks'
    __table_args__ = {'extend_existing': True}

    def __init__(self, Theme,Difficulty):
        self.Theme=Theme
        self.Difficulty=Difficulty

    Task_Id = Column(Integer, nullable=False, primary_key=True, unique=True)
    Theme = Column(VARCHAR(255), nullable=False)
    Difficulty = Column(Integer, nullable=False)

    @staticmethod
    def addNewInBase(TaskObject):
        connect.session.add(TaskObject)
        connect.session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Theme, Difficulty):
        newTask = Task(Theme,Difficulty)
        connect.session.add(newTask)
        connect.session.commit()
        return newTask


connect.Base.metadata.create_all(connect.engine)