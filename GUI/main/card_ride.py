# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_ride.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modify_L(object):
    def setupUi(self, modify_L):
        modify_L.setObjectName("modify_L")
        modify_L.resize(800, 601)
        self.OK = QtWidgets.QPushButton(modify_L)
        self.OK.setGeometry(QtCore.QRect(640, 480, 150, 46))
        self.OK.setObjectName("OK")
        self.Exit = QtWidgets.QPushButton(modify_L)
        self.Exit.setGeometry(QtCore.QRect(640, 540, 150, 46))
        self.Exit.setObjectName("Exit")
        self.textBrowser = QtWidgets.QTextBrowser(modify_L)
        self.textBrowser.setGeometry(QtCore.QRect(40, 400, 500, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.start_station_input = QtWidgets.QLineEdit(modify_L)
        self.start_station_input.setGeometry(QtCore.QRect(180, 30, 291, 20))
        self.start_station_input.setObjectName("start_station_input")
        self.start_station = QtWidgets.QLabel(modify_L)
        self.start_station.setGeometry(QtCore.QRect(30, 30, 150, 20))
        self.start_station.setObjectName("start_station")
        self.end_station_input = QtWidgets.QLineEdit(modify_L)
        self.end_station_input.setGeometry(QtCore.QRect(180, 70, 291, 20))
        self.end_station_input.setObjectName("end_station_input")
        self.end_station = QtWidgets.QLabel(modify_L)
        self.end_station.setGeometry(QtCore.QRect(30, 70, 150, 20))
        self.end_station.setObjectName("end_station")
        self.start_time_input = QtWidgets.QLineEdit(modify_L)
        self.start_time_input.setGeometry(QtCore.QRect(180, 110, 291, 20))
        self.start_time_input.setObjectName("start_time_input")
        self.start_time = QtWidgets.QLabel(modify_L)
        self.start_time.setGeometry(QtCore.QRect(30, 110, 150, 20))
        self.start_time.setObjectName("start_time")
        self.end_time_input = QtWidgets.QLineEdit(modify_L)
        self.end_time_input.setGeometry(QtCore.QRect(180, 150, 291, 20))
        self.end_time_input.setObjectName("end_time_input")
        self.end_time = QtWidgets.QLabel(modify_L)
        self.end_time.setGeometry(QtCore.QRect(30, 150, 150, 20))
        self.end_time.setObjectName("end_time")

        self.code_input = QtWidgets.QLineEdit(modify_L)
        self.code_input.setGeometry(QtCore.QRect(180, 190, 291, 20))
        self.code_input.setObjectName("code_input")
        self.code = QtWidgets.QLabel(modify_L)
        self.code.setGeometry(QtCore.QRect(30, 190, 150, 20))
        self.code.setObjectName("code")

        self.retranslateUi(modify_L)
        QtCore.QMetaObject.connectSlotsByName(modify_L)

    def retranslateUi(self, modify_L):
        _translate = QtCore.QCoreApplication.translate
        modify_L.setWindowTitle(_translate("modify_L", "Form"))
        self.OK.setText(_translate("modify_L", "OK"))
        self.Exit.setText(_translate("modify_L", "Exit"))
        self.start_station.setText(_translate("modify_L", "start_station:"))
        self.end_station.setText(_translate("modify_L", "end_station:"))
        self.start_time.setText(_translate("modify_L", "start_time:"))
        self.end_time.setText(_translate("modify_L", "end_time:"))
        self.code.setText(_translate("modify_L","code:"))
