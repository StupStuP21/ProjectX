import sqlalchemy
import Subject as sub
from sqlalchemy import Integer,  Column, VARCHAR, DATETIME, ForeignKey,REAL
from sqlalchemy.orm import relationship
from main import db
Subject = sub.Subject


class Lab(db.Base):
    __tablename__ = 'Labs'
    __table_args__ = {'extend_existing': True}

    def __init__(self, ID,Theme, DeadlineDate, MaxLScore, Subject_ID):
        self.Lab_Id = ID
        self.Theme = Theme
        self.DeadlineDate = DeadlineDate
        self.MaxLScore = MaxLScore
        self.Subject_ID = Subject_ID
        #self.connect = DatabaseConnect.engine.Connection

    Lab_Id = Column(Integer, nullable=False, primary_key=True, unique=True)
    Theme = Column(VARCHAR(255), nullable=False)
    DeadlineDate = Column(DATETIME, nullable=False)
    MaxLScore = Column(REAL, nullable=False)
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
        session = db.Session()
        session.add(LabObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(ID,Theme, DeadlineDate, MaxLScore,SID):
        session = db.Session()
        newLab = Lab(ID,Theme, DeadlineDate, MaxLScore,SID)
        session.add(newLab)
        session.commit()
        return newLab

    @staticmethod
    def test():
        print("Table is Alright")
        # return df

    @staticmethod
    def getAll_in_Subject(id):
        session = db.Session()
        q = db.getAllLabs()
        Labs = []
        for i in q:
            if (i[4]==id):
                Labs.append(Lab(i[0],i[1],i[2],i[3],i[4]))
        return Labs

    @staticmethod
    def getLabById(id):
        labs = db.getAllLabs()
        for i in labs:
            if i[0]==id:
                newLab = Lab(i[0],i[1],i[2],i[3],i[4])
                break
        return newLab


db.Base.metadata.create_all(db.engine)
