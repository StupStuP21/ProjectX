# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt6 import QtWidgets
from ui_main_window import Ui_MainWindow



# def connecting():
#     con = engine.connect()
#     metadata = MetaData()
#     # df = pnd.read_sql_query("SELECT * FROM dbo.Labs", con)
#     df = pnd.read_sql_query("SELECT * FROM HumanResources.Department", con)
#     print(df)


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
class StartWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = StartWindow() # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение



