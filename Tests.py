from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from DatabaseConnect import connect
from Subject import Subject


class Test(connect.Base):
    __tablename__ = 'Tests'
    __table_args__ = {'extend_existing': True}

    def __init__(self, MaxTScore, Subject_ID):
        self.Subject_ID = Subject_ID
        self.MaxTScore = MaxTScore

    Test_ID = Column(Integer, nullable=False, primary_key=True, unique=True)
    MaxTScore = Column(Integer, nullable=False)
    Subject_ID = Column(Integer, ForeignKey('Subjects.Subject_ID'))
    Subject = relationship(Subject)

    @staticmethod
    def addNewInBase(TestObject):
        connect.session.add(TestObject)
        connect.session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(MaxTScore, Subject_ID):
        newTest = Test(MaxTScore, Subject_ID)
        connect.session.add(newTest)
        connect.session.commit()
        return newTest


connect.Base.metadata.create_all(connect.engine)
