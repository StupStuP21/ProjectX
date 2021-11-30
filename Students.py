from sqlalchemy import Integer, Column, SMALLINT, VARCHAR
from DatabaseConnect import connect


class Student(connect.Base):
    __tablename__ = "Students"
    __table_args__ = {'extend_existing': True}
    Student_Id = Column(Integer, nullable=False, primary_key=True, unique=True)
    Name = Column(VARCHAR(255), nullable=False)
    Program = Column(VARCHAR(255), nullable=False)
    Course = Column(SMALLINT, nullable=False)

    def __init__(self, Name, Program, Course):
        self.Name = Name
        self.Program = Program
        self.Course = Course

    def getStudentId(self):
        return self.Student_Id

    def getName(self):
        return self.Name

    def getProgram(self):
        return self.Program

    def getCourse(self):
        return self.Course

    @staticmethod
    def addNewInBase(StudentObject):
        connect.session.add(StudentObject)
        connect.session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Name, Program, Course):
        newStudent = Student(Name, Program, Course)
        connect.session.add(newStudent)
        connect.session.commit()
        return newStudent


connect.Base.metadata.create_all(connect.engine)
