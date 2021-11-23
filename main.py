# This is a sample Python script.

from tkinter import *
import numpy as np
import pandas as pd
import pandas as pnd
import sqlalchemy as sal
from sqlalchemy import create_engine
import pyodbc




def readFiles(root):
    file1 = pnd.read_csv("LabsData.csv", header=0, delimiter=";")
    file2 = pnd.read_csv("TestAndTasksData.csv", header=0, delimiter=";")
    students = file1.iloc[:,0:4].values
    text = Text(root, height=50)
    text.pack()
    #text.insert(1.0, file1)
    text.insert(3.0, students)
    return students

def connecting2():
    engine = sal.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    #engine = sql.create_engine('mssql+pyodbc://LAPTOP-98I2O88V/ProjetX?driver=SQL_Server?Trusted_Connection=yes')
    conn = engine.connect()
    conn.execute("select * from Student")
def connecting():
    Driver = 'ODBC Driver 17 for SQL Server'
    Server = 'DESKTOP-0ED7FI8\SQLEXPRESS'
    #port = 'PORT=1433'
    Database = 'Students'

    Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'
    engine = create_engine(Database_con)
    con = engine.connect()
    df = pd.read_sql_query("SELECT * FROM dbo.Users", con)
    print(df)

    #conn_str = ';'.join([driver, server,db])
    #conn = pyodbc.connect(conn_str)
    #return conn
    #cursor = conn.cursor()
    #cursor.execute('select * from Labs')
    #rows = cursor.fetchall()
    #strings = []

    #for string in cursor.fetchall():
     #   columns = []
      #  columns = string.split(",", 1)
      #  row = cursor.fetchone()
       # for i in columns:
        #    strings.append(columns[i])
    #print(strings)
    #text = Text(root, height=50)
    #text.pack()
    #text.insert(1.0, strings)

def InsertingStudents(root):
    conn = connecting()
    cursor = conn.cursor()
    student = readFiles(root)
    params = []
    for i in range(len(student)):
        params.append(student[i])
    for p in params:
        print(p)
        cursor.execute("insert into Student (Student_Id,Name_,Programm,Course) values (?,?,?,?)", p)

def conn():
    conn = pyodbc.connect(
        r'Driver={SQL Server};Server=DESKTOP-0ED7FI8\SQLEXPRESS;Database=Students;Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM dbo.Users')
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.name)
    conn.close()



if __name__ == '__main__':
    root = Tk()
    #b1 = Button(text="Распечатать",
    #               width=15, height=3, command=readFiles(root))
    # b1.pack()
    b2 = Button(text="Подключиться",
                  width=15, height=3, command=connecting())
    b2.pack()
    root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
