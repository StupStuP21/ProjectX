﻿# Form implementation generated from reading ui file 'ui_main_window.ui'
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
        self.studid_label = QtWidgets.QLabel(self.tab_predict)
        self.studid_label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.studid_label.setObjectName("studid_label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_predict)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.subject_label = QtWidgets.QLabel(self.tab_predict)
        self.subject_label.setGeometry(QtCore.QRect(140, 10, 47, 13))
        self.subject_label.setObjectName("subject_label")
        self.comboBox_subject = QtWidgets.QComboBox(self.tab_predict)
        self.comboBox_subject.setGeometry(QtCore.QRect(140, 30, 69, 21))
        self.comboBox_subject.setObjectName("comboBox_subject")
        self.predict_button = QtWidgets.QPushButton(self.tab_predict)
        self.predict_button.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.predict_button.setObjectName("predict_button")
        self.text_predict_edit = QtWidgets.QTextEdit(self.tab_predict)
        self.text_predict_edit.setGeometry(QtCore.QRect(220, 30, 541, 501))
        self.text_predict_edit.setReadOnly(True)
        self.text_predict_edit.setObjectName("text_predict_edit")
        self.test_label = QtWidgets.QLabel(self.tab_predict)
        self.test_label.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.test_label.setObjectName("test_label")
        self.comboBox_text = QtWidgets.QComboBox(self.tab_predict)
        self.comboBox_text.setGeometry(QtCore.QRect(140, 80, 69, 21))
        self.comboBox_text.setObjectName("comboBox_text")
        self.tabWidget.addTab(self.tab_predict, "")
        self.tab_stat = QtWidgets.QWidget()
        self.tab_stat.setObjectName("tab_stat")
        self.graphicsViewForGraf = QtWidgets.QGraphicsView(self.tab_stat)
        self.graphicsViewForGraf.setGeometry(QtCore.QRect(260, 30, 511, 511))
        self.graphicsViewForGraf.setObjectName("graphicsViewForGraf")
        self.graf_label = QtWidgets.QLabel(self.tab_stat)
        self.graf_label.setGeometry(QtCore.QRect(260, 10, 121, 16))
        self.graf_label.setObjectName("graf_label")
        self.tabWidget.addTab(self.tab_stat, "")
        self.tab_something_else = QtWidgets.QWidget()
        self.tab_something_else.setObjectName("tab_something_else")
        self.tabWidget.addTab(self.tab_something_else, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.studid_label.setText(_translate("MainWindow", "StudId"))
        self.subject_label.setText(_translate("MainWindow", "Предмет"))
        self.predict_button.setText(_translate("MainWindow", "Стратегия"))
        self.test_label.setText(_translate("MainWindow", "Контрольная"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_predict), _translate("MainWindow", "Советы по решению контрольных"))
        self.graf_label.setText(_translate("MainWindow", "График чего-нибудь"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stat), _translate("MainWindow", "Статистика"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_something_else), _translate("MainWindow", "Хз"))