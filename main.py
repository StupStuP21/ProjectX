# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt6 import QtWidgets
from main_window import Ui_MainWindow
import sqlalchemy
import sqlalchemy.orm as sql
from DatabaseConnect import DatabaseConnect
from threading import Thread
from SubjectModel import subjectModel
from TestModel import testModel

class StartWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_subject.activated.connect(comboboxSubjectChanged)


def setSubjects():
    subjects = [str(subjectModel(s)) for s in db.getAllSubjects()]
    window.comboBox_subject.addItems(subjects)

def comboboxSubjectChanged():
    subject = window.comboBox_subject.currentText()
    tests = db.getAllTestsBySubjectName(subject)
    testsModels = [testModel(s) for s in tests]
    testsIds = [str(test) for test in testsModels]
    window.comboBox_text.addItems(testsIds)


if __name__ == '__main__':
    db = DatabaseConnect()
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    setSubjects()
    app.exec()
    #subjects = [str(sub(s)) for s in db.getAllSubjects()]









