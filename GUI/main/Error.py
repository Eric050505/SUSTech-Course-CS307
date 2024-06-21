# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#
# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_Error(object):
#     def setupUi(self, Error):
#         Error.setObjectName("Error")
#         Error.resize(400, 300)
#         self.tips = QtWidgets.QLabel(Error)
#         self.tips.setGeometry(QtCore.QRect(30, 120, 350, 40))
#         self.tips.setStyleSheet("font: 15pt \"Arial\";")
#         self.tips.setObjectName("tips")
#
#         self.retranslateUi(Error)
#         QtCore.QMetaObject.connectSlotsByName(Error)
#
#     def retranslateUi(self, Error):
#         _translate = QtCore.QCoreApplication.translate
#         Error.setWindowTitle(_translate("Error", "Form"))
#         self.tips.setText(_translate("Error", "Please check your input"))


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(400, 300)
        self.tips = QtWidgets.QLabel(Error)
        self.tips.setGeometry(QtCore.QRect(30, 120, 350, 40))
        self.tips.setStyleSheet("font: 15pt \"Arial\";")
        self.tips.setObjectName("tips")

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Form"))
        self.tips.setText(_translate("Error", "Please check your input"))

    # 添加 resizeEvent 方法处理窗口大小变化事件
    def resizeEvent(self, event):
        # 根据窗口大小调整标签大小
        window_width = event.size().width()
        window_height = event.size().height()

        # 根据窗口宽度等比例调整组件大小
        label_width = window_width - 50
        label_height = window_height // 4
        label_font_size = label_height // 5

        self.tips.setGeometry(QtCore.QRect(30, window_height // 3, label_width, label_height))
        self.tips.setStyleSheet(f"font: {label_font_size}pt \"Arial\";")