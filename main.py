# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import Controller
from PyQt6 import QtWidgets
from main_window import Ui_MainWindow
import sqlalchemy
import sqlalchemy.orm as sql
from DatabaseConnect import DatabaseConnect
from threading import Thread

db = DatabaseConnect()

class StartWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class sub:
    def __init__(self, tup):
        self.id = tup[0]
        self.name = tup[1]
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

def setSubjects():
    subjects = [str(sub(s)) for s in db.getAllSubjects()]
    window.comboBox_subject.addItems(subjects)
    window.subject_label.setText("Suqqa")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    #Controller.test()
    window.show()
    setSubjects()
    app.exec()
    subjects = [str(sub(s)) for s in db.getAllSubjects()]
    print(subjects)









