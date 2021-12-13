from sqlalchemy import Integer, Column, ForeignKey,Date
from sqlalchemy.orm import relationship
from main import db
from Students import Student
from Labs import Lab

class CompletedLab(db.Base):
    __tablename__ = 'LabStud'
    __table_args__ = {'extend_existing': True}

    def __init__(self, Stud_ID, Lab_ID,Tryes,PassDate,GetLScore):
        self.Stud_ID = Stud_ID
        self.Lab_ID = Lab_ID
        self.Tryes = Tryes
        self.PassDate = PassDate
        self.GetLScore = GetLScore

    Stud_ID = Column(Integer,ForeignKey('Students.Student_Id'), primary_key=True,unique=True)
    Lab_ID = Column(Integer,ForeignKey('Labs.Lab_Id'), primary_key=True,unique=True)
    Tryes = Column(Integer, nullable=False)
    PassDate=Column(Date,nullable=True)
    GetLScore=Column(Integer,nullable=False)
    Students = relationship(Student)
    Labs = relationship(Lab)

    @staticmethod
    def addNewInBase(CompletedLabObject):
        session = db.Session()
        session.add(CompletedLabObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Stud_ID, Lab_ID,Tryes,PassDate,GetLScore):
        session = db.Session()
        newCompletedLab = CompletedLab(Stud_ID, Lab_ID,Tryes,PassDate,GetLScore)
        session.add(newCompletedLab)
        session.commit()
        return newCompletedLab

    @staticmethod
    def getAllCompletedLabsByStudId(sid):
        allLabs = db.getAllLabStud()
        LabsCurrent=[]
        for i in allLabs:
            if i[0] == sid:
                newCompletedLab = CompletedLab(i[0],i[1],i[2],i[3],i[4])
                LabsCurrent.append(newCompletedLab)
        return LabsCurrent

    @staticmethod
    def getAllCompletedLabsWithoutByStudId(sid):
        allLabs = db.getAllLabStud()
        LabsCurrent = []
        for i in allLabs:
            if i[0] != sid:
                newCompletedLab = CompletedLab(i[0], i[1], i[2], i[3], i[4])
                LabsCurrent.append(newCompletedLab)
        return LabsCurrent

    @staticmethod
    def getAllCompletedLabsWithoutByStudIdWithByStudId(sid,wsid):
        allLabs = db.getAllLabStud()
        LabsCurrent = []
        for i in allLabs:
            if i[0] != wsid and i[0] == sid:
                newCompletedLab = CompletedLab(i[0], i[1], i[2], i[3], i[4])
                LabsCurrent.append(newCompletedLab)
        return LabsCurrent

    def Print(self):
        print ('stud_id:',self.Stud_ID,' lab_id:',self.Lab_ID,'PassDate:',self.PassDate,'Tryes:',self.Tryes,'Score:',self.GetLScore)

db.Base.metadata.create_all(db.engine)