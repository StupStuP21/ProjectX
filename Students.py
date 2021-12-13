from sqlalchemy import Integer, Column, SMALLINT, VARCHAR

#from CompletedTasks import CompletedTask
from main import db


class Student(db.Base):
    __tablename__ = "Students"
    __table_args__ = {'extend_existing': True}
    Student_Id = Column(Integer, nullable=False, primary_key=True, unique=True)
    Name = Column(VARCHAR(255), nullable=False)
    Program = Column(VARCHAR(255), nullable=False)
    Course = Column(SMALLINT, nullable=False)

    def __init__(self, Id, Name, Program, Course):
        self.Student_Id = Id
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
        session = db.Session()
        session.add(StudentObject)
        session.commit()

    @staticmethod
    def Create_AddInBase_GetObject(Name, Program, Course):
        session = db.Session()
        newStudent = Student(Name, Program, Course)
        session.add(newStudent)
        session.commit()
        return newStudent

    @staticmethod
    def getStudentById(id):
        session = db.Session()
        students = db.getAllStudents()
        for i in students:
            if i[0] == id:
                student = i
                newStudent = Student(i[0], i[1], i[2], i[3])
                break
        return newStudent

    @staticmethod
    def getStudentsWithoutById(id):
        students = db.getAllStudents()
        Studs = []
        for i in students:
            if i[0] != id:
                newStudent = Student(i[0], i[1], i[2], i[3])
                Studs.append(newStudent)
        return Studs

    def Print(self):
        print("Student_ID: ", self.Student_Id, ";", "Name: ", self.Name, ";", "Program: ", self.Program, ";",
              "Course: ", self.Course)




db.Base.metadata.create_all(db.engine)
