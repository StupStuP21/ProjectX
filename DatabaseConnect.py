from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import *
import sqlalchemy
from sqlalchemy.orm import *

class DatabaseConnect:
    def getAll(self, table):
        session = self.Session()
        out = []
        q = session.query(table)
        for c in q:
            out.append(c)
        return out

    def getAllLabs(self):
        return self.getAll(self.labs_table)

    def getAllLabStud(self):
        return self.getAll(self.labs_table)

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

    def __init__(self):
        self.engine = create_engine(
            'mssql://ПК\\SQLEXPRESS/ProjectXX?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server')
        self.engine.connect()
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




