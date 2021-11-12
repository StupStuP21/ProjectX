
import sqlalchemy
import pyodbc
from sqlalchemy import MetaData, Integer, String, create_engine, Column, SMALLINT, VARCHAR


class Student(object):
    __tablename__="Students"

    Student_Id = Column(Integer,nullable=False,primary_key=True,unique=True)
    Name_ = Column(VARCHAR(50),nullable=False)
    Program = Column(VARCHAR(50),nullable=False)
    Course = Column(SMALLINT,nullable=False)
