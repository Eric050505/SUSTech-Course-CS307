# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_unf_c_rides.ui'
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

        self.retranslateUi(modify_L)
        QtCore.QMetaObject.connectSlotsByName(modify_L)

    def retranslateUi(self, modify_L):
        _translate = QtCore.QCoreApplication.translate
        modify_L.setWindowTitle(_translate("modify_L", "Form"))
        self.OK.setText(_translate("modify_L", "OK"))
        self.Exit.setText(_translate("modify_L", "Exit"))
