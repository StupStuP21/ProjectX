import sqlalchemy
import pyodbc
import Subject as sub
from sqlalchemy import MetaData, Integer, String, create_engine, Column, SMALLINT, VARCHAR,DATETIME,ForeignKey
from sqlalchemy.orm import declarative_base,Session,relationship
from main import engine,Base,session

Subject = sub.Subject
class Lab(Base):
    __tablename__='Labs'
    __table_args__ = {'extend_existing': True}
    def __init__(self, Theme, DeadlineDate,MaxLScore,Subject_ID):
        self.Theme = Theme
        self.DeadlineDate = DeadlineDate
        self.MaxLScore = MaxLScore
        self.Subject_ID = Subject_ID

    Lab_ID = Column(Integer,nullable=False,primary_key=True,unique=True)
    Theme = Column(VARCHAR(255),nullable=False)
    DeadlineDate = Column(DATETIME,nullable=False)
    MaxLScore = Column(Integer,nullable=False)
    Subject_ID = Column(Integer,ForeignKey('Subjects.Subject_ID'))
    Subject = relationship(Subject)

    def getLabId(self):
        return self.Lab_ID

    def getTheme(self):
        return self.Theme

    def getDeadline(self):
        return self.DeadlineDate

    def getMaxScore(self):
        return self.MaxLScore

    def getSubjectId(self):
        return self.Subject_ID

    @staticmethod
    def addNewLabInBase(LabObject):
        session.add(LabObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Theme,DeadlineDate,MaxLScore):
        newLab = Lab(Theme,DeadlineDate,MaxLScore)
        session.add(newLab)
        session.commit()
        return newLab

    @staticmethod
    def test():
        print("Table is Alright")
        #return df
Base.metadata.create_all(engine)