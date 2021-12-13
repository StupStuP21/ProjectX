from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from main import db
from Subject import Subject


class Test(db.Base):
    __tablename__ = 'Tests'
    __table_args__ = {'extend_existing': True}

    def __init__(self, test_Id,MaxTScore, Subject_ID):
        self.Test_ID = test_Id
        self.Subject_ID = Subject_ID
        self.MaxTScore = MaxTScore

    Test_ID = Column(Integer, nullable=False, primary_key=True, unique=True)
    MaxTScore = Column(Integer, nullable=False)
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


db.Base.metadata.create_all(db.engine)
