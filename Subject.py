import sqlalchemy
import pyodbc
from sqlalchemy import MetaData, Integer, String, create_engine, Column, SMALLINT, VARCHAR


class Subject(object):
    __tablename__="Subjects"

    Subject_ID = Column(Integer,nullable=False,primary_key=True,unique=True)
    Name = Column(VARCHAR(50),nullable=False)