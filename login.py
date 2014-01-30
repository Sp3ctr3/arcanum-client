# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lazarus.ui'
#
# Created: Fri Jan 31 00:21:45 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.Login = QtGui.QPushButton(Dialog)
        self.Login.setGeometry(QtCore.QRect(270, 240, 98, 27))
        self.Login.setObjectName(_fromUtf8("Login"))
        self.username = QtGui.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(120, 70, 161, 27))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(120, 110, 161, 27))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.register_2 = QtGui.QPushButton(Dialog)
        self.register_2.setGeometry(QtCore.QRect(30, 240, 98, 27))
        self.register_2.setObjectName(_fromUtf8("register_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.address = QtGui.QLineEdit(Dialog)
        self.address.setGeometry(QtCore.QRect(120, 150, 161, 27))
        self.address.setObjectName(_fromUtf8("address"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Login.setText(_translate("Dialog", "Login", None))
        self.register_2.setText(_translate("Dialog", "Register", None))
        self.label.setText(_translate("Dialog", "Username", None))
        self.label_2.setText(_translate("Dialog", "Password", None))
        self.label_3.setText(_translate("Dialog", "Server", None))

