# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passenger_info.ui'
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
        self.passenger_id = QtWidgets.QLabel(modify_L)
        self.passenger_id.setGeometry(QtCore.QRect(40, 40, 150, 20))
        self.passenger_id.setObjectName("passenger_id")
        self.OK = QtWidgets.QPushButton(modify_L)
        self.OK.setGeometry(QtCore.QRect(640, 480, 150, 46))
        self.OK.setObjectName("OK(passenger)")
        self.OK2 = QtWidgets.QPushButton(modify_L)
        self.OK2.setGeometry(QtCore.QRect(640, 380, 150, 46))
        self.OK2.setObjectName("OK(card)")
        self.Exit = QtWidgets.QPushButton(modify_L)
        self.Exit.setGeometry(QtCore.QRect(640, 540, 150, 46))
        self.Exit.setObjectName("Exit")
        self.textBrowser = QtWidgets.QTextBrowser(modify_L)
        self.textBrowser.setGeometry(QtCore.QRect(40, 440, 500, 150))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser2 = QtWidgets.QTextBrowser(modify_L)
        self.textBrowser2.setGeometry(QtCore.QRect(40, 280, 500, 150))
        self.textBrowser2.setObjectName("textBrowser2")
        self.passenger_id_input = QtWidgets.QLineEdit(modify_L)
        self.passenger_id_input.setGeometry(QtCore.QRect(190, 40, 291, 20))
        self.passenger_id_input.setObjectName("passenger_id_input")
        self.card_code_input = QtWidgets.QLineEdit(modify_L)
        self.card_code_input.setGeometry(QtCore.QRect(190, 80, 291, 20))
        self.card_code_input.setObjectName("card_code_input")
        self.card_code = QtWidgets.QLabel(modify_L)
        self.card_code.setGeometry(QtCore.QRect(40, 80, 150, 20))
        self.card_code.setObjectName("card_code")
        self.start_station_input = QtWidgets.QLineEdit(modify_L)
        self.start_station_input.setGeometry(QtCore.QRect(190, 120, 291, 20))
        self.start_station_input.setObjectName("start_station_input")
        self.start_station = QtWidgets.QLabel(modify_L)
        self.start_station.setGeometry(QtCore.QRect(40, 120, 150, 20))
        self.start_station.setObjectName("start_station")
        self.end_station_input = QtWidgets.QLineEdit(modify_L)
        self.end_station_input.setGeometry(QtCore.QRect(190, 160, 291, 20))
        self.end_station_input.setObjectName("end_station_input")
        self.end_station = QtWidgets.QLabel(modify_L)
        self.end_station.setGeometry(QtCore.QRect(40, 160, 150, 20))
        self.end_station.setObjectName("end_station")
        self.start_time_input = QtWidgets.QLineEdit(modify_L)
        self.start_time_input.setGeometry(QtCore.QRect(190, 200, 291, 20))
        self.start_time_input.setObjectName("start_time_input")
        self.start_time = QtWidgets.QLabel(modify_L)
        self.start_time.setGeometry(QtCore.QRect(40, 200, 150, 20))
        self.start_time.setObjectName("start_time")
        self.end_time_input = QtWidgets.QLineEdit(modify_L)
        self.end_time_input.setGeometry(QtCore.QRect(190, 240, 291, 20))
        self.end_time_input.setObjectName("end_time_input")
        self.end_time = QtWidgets.QLabel(modify_L)
        self.end_time.setGeometry(QtCore.QRect(40, 240, 150, 20))
        self.end_time.setObjectName("end_time")

        self.retranslateUi(modify_L)
        QtCore.QMetaObject.connectSlotsByName(modify_L)

    def retranslateUi(self, modify_L):
        _translate = QtCore.QCoreApplication.translate
        modify_L.setWindowTitle(_translate("modify_L", "Form"))
        self.passenger_id.setText(_translate("modify_L", "passenger_id:"))
        self.OK.setText(_translate("modify_L", "OK(passenger)"))
        self.OK2.setText(_translate("modify_L", "OK(card)"))
        self.Exit.setText(_translate("modify_L", "Exit"))
        self.card_code.setText(_translate("modify_L", "card_code:"))
        self.start_station.setText(_translate("modify_L", "start_station:"))
        self.end_station.setText(_translate("modify_L", "end_station:"))
        self.start_time.setText(_translate("modify_L", "start_time:"))
        self.end_time.setText(_translate("modify_L", "end_time:"))
