import sqlalchemy
import pyodbc
from sqlalchemy import MetaData, Integer, String, create_engine, Column, SMALLINT, VARCHAR


class Lab(object):
    __tablename__="Labs"

    Lab_ID = Column(Integer,nullable=False,primary_key=True,unique=True)
    Theme = Column(VARCHAR(255),nullable=False)
    DeadlineDate = Column(Date,nullable=False)
    MaxLScore = Column(Integer,nullable=False)