# Form implementation generated from reading ui file '.\ui_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 781, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_predict = QtWidgets.QWidget()
        self.tab_predict.setObjectName("tab_predict")
        self.label = QtWidgets.QLabel(self.tab_predict)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_predict)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_predict)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 47, 13))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_predict)
        self.comboBox.setGeometry(QtCore.QRect(140, 30, 69, 21))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.tab_predict)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.tab_predict)
        self.textEdit.setGeometry(QtCore.QRect(220, 30, 541, 501))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_predict, "")
        self.tab_stat = QtWidgets.QWidget()
        self.tab_stat.setObjectName("tab_stat")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_stat)
        self.graphicsView.setGeometry(QtCore.QRect(320, 30, 451, 511))
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.tab_stat)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 121, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_stat, "")
        self.tab_something_else = QtWidgets.QWidget()
        self.tab_something_else.setObjectName("tab_something_else")
        self.tabWidget.addTab(self.tab_something_else, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "StudId"))
        self.label_2.setText(_translate("MainWindow", "Предмет"))
        self.pushButton.setText(_translate("MainWindow", "Стратегия"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_predict), _translate("MainWindow", "Советы по решению контрольных"))
        self.label_3.setText(_translate("MainWindow", "Какой-нибудь график"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stat), _translate("MainWindow", "Статистика"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_something_else), _translate("MainWindow", "Что-нибудь еще"))