# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import Controller
from PyQt6 import QtWidgets

#from ForGraphics import ForGraphics1
import Filtering
from Graphic1 import PlotCanvas
from main_window import Ui_MainWindow
from DatabaseConnect import DatabaseConnect
#from NumberOfTaskInTest import NumberInTest


db = DatabaseConnect()
from taskWsDto import getTaskWsDtoListMock


class StartWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        scores, koeffs = Controller.forGraphic()
        self.m = PlotCanvas(parent=self.tab_stat, width=5, height=4, scores=scores, koeffs=koeffs)
        self.m.move(140, 30)
class sub:
    def __init__(self, tup):
        self.id = tup[0]
        self.name = tup[1]
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
class test:
    def __init__(self,tup):
        self.id = tup[0]
        self.theme = str(tup[3])

    def __str__(self):
        return self.theme

    def __repr__(self):
        return self.theme

def setSubjects():
    subjects = [str(sub(s)) for s in db.getAllSubjects()]
    window.comboBox_subject.addItems(subjects)

def get_Predict():
    pass

def test_predict(road,queueOfNumbers):

    return Controller.forTest(road, queueOfNumbers)

def predictButtonListener():

    #studId,subId,testId
    subjectName = window.comboBox_subject.currentText()
    studId = int(window.lineEdit.text())
    testName = window.comboBox_text.currentText()
    testObject = db.getTestByName(testName)
    print(testObject.id)
    subjectObject = db.getSubjectByName(subjectName)
    road = Filtering.Filterisation(studId,subjectObject.id,2).main() #<-------------место 2 подставить тестid
    tasksWsDtoList = Controller.forTest(road,2) #<-------------место 2 подставить тестid
    window.text_predict_edit.setText("\tНомер\tНомер в контрольной\tТема\n")
    for task in tasksWsDtoList:
        line = "\t" + str(task.TaskQueueInOutput) + "\t"*2 + str(task.TaskQueue) + "\t" + task.Theme+"\n"
        window.text_predict_edit.setText(window.text_predict_edit.toPlainText() + line)

def subjectComboboxChanged():
    try:
        subjects = [str(test(s)) for s in db.getAllTestsBySubjectName(window.comboBox_subject.currentText())]
        window.comboBox_text.clear()
        window.comboBox_text.addItems(subjects)
    except Exception:
        print(Exception.__text_signature__)

def graph():
    pass
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.predict_button.clicked.connect(predictButtonListener)
    window.comboBox_subject.currentIndexChanged.connect(subjectComboboxChanged)
    #Controller.test()
    #Controller.forGraphic()
    window.show()

    setSubjects()
    app.exec()











