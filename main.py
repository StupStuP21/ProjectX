# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *
import numpy as np
import pandas as pnd
import pyodbc
import sqlalchemy as sql
import Controller
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, MetaData, null

Driver = 'ODBC Driver 17 for SQL Server'
# Server = 'DESKTOP-0ED7FI8\SQLEXPRESS'
Server = 'LAPTOP-98I2O88V'
# port = 'PORT=1433'
Database = 'ProjectXX'
# Database = 'AdventureWorks2019'

Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'
engine = create_engine(Database_con)
Base = declarative_base()
session = Session(bind=engine)
def readFiles():
    file1 = pnd.read_csv("LabsData.csv", header=0, delimiter=";")
    file2 = pnd.read_csv("TestAndTasksData.csv", header=0, delimiter=";")
    students = file1.iloc[:, 0:4].values
    text = Text(root, height=50)
    text.pack()
    text.insert(1.0, file1)
    text.insert(3.0, file2)
    # return students


def connecting():
    con = engine.connect()
    metadata = MetaData()
    # df = pnd.read_sql_query("SELECT * FROM dbo.Labs", con)
    df = pnd.read_sql_query("SELECT * FROM HumanResources.Department", con)
    print(df)


# def connecting2():
#     engine = sql.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
#     #engine = sql.create_engine('mssql+pyodbc://LAPTOP-98I2O88V/ProjetX?driver=SQL_Server?Trusted_Connection=yes')
#     conn = engine.connect()
#     conn.execute("select * from Student")
# def connecting():
# driver = 'DRIVER={SQL Server}'
# server = 'SERVER=LAPTOP-98I2O88V'
# #port = 'PORT=1433'
# db = 'DATABASE=ProjetX'
# #user = 'UID=sa'
# #pw = 'PWD=111111111111111'
# conn_str = ';'.join([driver, server,db])
# conn = pyodbc.connect(conn_str)
# return conn
# #cursor = conn.cursor()
# #cursor.execute('select * from Labs')
# #rows = cursor.fetchall()
# #strings = []
#
# #for string in cursor.fetchall():
#  #   columns = []
#   #  columns = string.split(",", 1)
#   #  row = cursor.fetchone()
#    # for i in columns:
#     #    strings.append(columns[i])
# #print(strings)
# #text = Text(root, height=50)
# #text.pack()
# #text.insert(1.0, strings)

# def InsertingStudents(root):
#     conn = connecting()
#     cursor = conn.cursor()
#     student = readFiles(root)
#     params = []
#     for i in range(len(student)):
#         params.append(student[i])
#     for p in params:
#         print(p)
#         cursor.execute("insert into Student (Student_Id,Name_,Programm,Course) values (?,?,?,?)", p)
# def thirdFunction():
#     pass
    # newLab = Lab(Theme = 'GR', DeadlineDate='2021-07-11', MaxLScore=12,Subject_ID=1)
    # Labs.Lab.addNewLabInBase(newLab)
    # Labs.Lab.test()
    # Lab = Labs.Lab.getLabTroughId(1)
    # print(Lab)


if __name__ == '__main__':
    root = Tk()
    b1 = Button(text="Распечатать",
                width=15, height=3, command=readFiles)
    b1.pack()
    b2 = Button(text="Подключиться",
                width=15, height=3, command=connecting)
    b2.pack()
    b3 = Button(text="Получить лабу",
                width=15, height=3, command=Controller.test)
    b3.pack()
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
