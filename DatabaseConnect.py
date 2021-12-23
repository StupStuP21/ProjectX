from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import *
import sqlalchemy
from sqlalchemy.orm import *
from SubjectModel import subjectModel
from TestModel import testModel
class DatabaseConnect:
    def getAll(self, table):
        session = self.Session()
        out = []
        q = session.query(table)
        for c in q:
            out.append(c)
        session.close()
        return out

    def getAllWithout(self,table,id):
        session = self.Session()
        out=[]
        q = session.query(table).filter_by(table.Lab_Id!=id).all()
        for c in q:
            out.append(c)
        return out

    def getAllLabs(self):
        return self.getAll(self.labs_table)

    def getAllLabsWithout(self,id):
        return self.getAllWithout(self.labs_table,id)

    def getAllLabStud(self):
        return self.getAll(self.lab_stud_table)

    def getAllStudents(self):
        return self.getAll(self.students_table)

    def getAllSubjects(self):
        return self.getAll(self.subjects_table)

    def getAllTasks(self):
        return self.getAll(self.tasks_table)

    def getAllTests(self):
        return self.getAll(self.tests_table)

    def getAllTestStud(self):
        return self.getAll(self.test_stud_table)

    def getAllTestTaskStud(self):
        return self.getAll(self.test_task_stud_table)

    def getAllTestsBySubjectName(self, subject):
        subject = self.getSubjectByName(subject)
        session = self.Session()
        q = session.query(self.tests_table).filter(self.tests_table.c.Subject_Id == subject.id)
        #q = session.query(self.tests_table)
        a = []
        for c in q:
            a.append(c)
        return a

    def getSubjectByName(self, name):
        session = self.Session()
        return subjectModel(session.query(self.subjects_table).filter(self.subjects_table.c.Name == name).first())
        #filter(self.subjects_table.name == name).first()

    def getTestByName(self, name):
        session = self.Session()
        test = testModel(session.query(self.tests_table).filter(self.tests_table.c.Name == name).first())
        return test


    def __init__(self):
        self.engine = create_engine(
            'mssql://LAPTOP-98I2O88V/ProjectXX?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server')
            #'mssql://ПК\\SQLEXPRESS/ProjectXX?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server')
        self.engine.connect()
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.metadata = MetaData(bind=self.engine)
        self.labs_table = sqlalchemy.Table('Labs', self.metadata, autoload=True)
        self.lab_stud_table = sqlalchemy.Table("LabStud", self.metadata, autoload=True)
        self.students_table = sqlalchemy.Table("Students", self.metadata, autoload=True)
        self.subjects_table = sqlalchemy.Table("Subjects", self.metadata, autoload=True)
        self.tasks_table = sqlalchemy.Table("Tasks", self.metadata, autoload=True)
        self.tests_table = sqlalchemy.Table("Tests", self.metadata, autoload=True)
        self.test_stud_table = sqlalchemy.Table("TestStud", self.metadata, autoload=True)
        self.test_task_stud_table = sqlalchemy.Table("TestTaskStud", self.metadata, autoload=True)




