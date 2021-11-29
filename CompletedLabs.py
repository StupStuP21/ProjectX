from sqlalchemy import Integer, Column, ForeignKey,Date
from sqlalchemy.orm import relationship
from DatabaseConnect import connect
from Students import Student
from Labs import Lab

class CompletedLab(connect.Base):
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
        connect.session.add(CompletedLabObject)
        connect.session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Stud_ID, Lab_ID,Tryes,PassDate,GetLScore):
        newCompletedLab = CompletedLab(Stud_ID, Lab_ID,Tryes,PassDate,GetLScore)
        connect.session.add(newCompletedLab)
        connect.session.commit()
        return newCompletedLab


connect.Base.metadata.create_all(connect.engine)