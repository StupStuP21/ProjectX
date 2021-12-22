# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
#import Controller
from PyQt6 import QtWidgets
from PyQt6.QtCore import QEvent
from PyQt6.QtGui import QAction

from main_window import Ui_MainWindow
import matplotlib as plt
import sqlalchemy
import sqlalchemy.orm as sql
from DatabaseConnect import DatabaseConnect
from threading import Thread

#db = DatabaseConnect()
from taskWsDto import getTaskWsDtoListMock


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

def get_Predict():
    pass

def test_predict():
    return getTaskWsDtoListMock(1,1,1)

def predictButtonListener():
    tasksWsDtoList = test_predict()
    window.text_predict_edit.setText("\tНомер\tНомер в контрольной\tТема\n")
    for task in tasksWsDtoList:
        line = "\t" + str(task.TaskQueueInOutput) + "\t"*2 + str(task.TaskQueue) + "\t" + task.Theme+"\n"
        window.text_predict_edit.setText(window.text_predict_edit.toPlainText() + line)

def graph():
    pass
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = []
    c = [1,2,3]
    b = [3,2,1]
    for i in range(10):
        lab = "Some Text"

        a.append(lab)


    window = StartWindow()
    #window.text_predict_edit.setText("\n".join(a))
    #act = QAction(predictButtonListener)
   # elf.menu = QMenu()
    #self.action = QAction("Exit")
    #self.menu.addAction(self.action)
    #self.action.triggered.connect(self.my_function)
    #window.predict_button.actionEvent(QAction(predictButtonListener))
    window.predict_button.clicked.connect(predictButtonListener)

    #window.predict_button.actions().
    #Controller.test()
    #Controller.forGraphic()
    window.show()

    #setSubjects()
    app.exec()











