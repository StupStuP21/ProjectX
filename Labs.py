import DatabaseConnect.engine
import sqlalchemy
import Subject as sub
from sqlalchemy import Integer,  Column, VARCHAR, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

Subject = sub.Subject


class Lab:
    __tablename__ = 'Labs'
    __table_args__ = {'extend_existing': True}

    def __init__(self, Theme, DeadlineDate, MaxLScore, Subject_ID):
        self.Theme = Theme
        self.DeadlineDate = DeadlineDate
        self.MaxLScore = MaxLScore
        self.Subject_ID = Subject_ID
        self.connect = DatabaseConnect.engine.Connection

    Lab_Id = Column(Integer, nullable=False, primary_key=True, unique=True)
    Theme = Column(VARCHAR(255), nullable=False)
    DeadlineDate = Column(DATETIME, nullable=False)
    MaxLScore = Column(Integer, nullable=False)
    Subject_ID = Column(Integer, ForeignKey('Subjects.Subject_ID'))
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
    def addNewInBase(LabObject):
        connect.session.add(LabObject)
        connect.session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Theme, DeadlineDate, MaxLScore):
        newLab = Lab(Theme, DeadlineDate, MaxLScore)
        connect.session.add(newLab)
        connect.session.commit()
        return newLab

    @staticmethod
    def test():
        print("Table is Alright")
        # return df


connect.Base.metadata.create_all(connect.engine)
