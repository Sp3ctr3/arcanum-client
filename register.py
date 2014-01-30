# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created: Thu Jan 30 22:31:12 2014
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
        Dialog.resize(417, 313)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1021, 741))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.username = QtGui.QLineEdit(self.tab)
        self.username.setGeometry(QtCore.QRect(200, 40, 181, 27))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(self.tab)
        self.password.setGeometry(QtCore.QRect(200, 80, 181, 27))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.password2 = QtGui.QLineEdit(self.tab)
        self.password2.setGeometry(QtCore.QRect(200, 120, 181, 27))
        self.password2.setEchoMode(QtGui.QLineEdit.Password)
        self.password2.setObjectName(_fromUtf8("password2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(70, 40, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 131, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.RegisterButton = QtGui.QPushButton(self.tab)
        self.RegisterButton.setGeometry(QtCore.QRect(290, 200, 98, 27))
        self.RegisterButton.setObjectName(_fromUtf8("RegisterButton"))
        self.email = QtGui.QLineEdit(self.tab)
        self.email.setGeometry(QtCore.QRect(200, 160, 181, 27))
        self.email.setObjectName(_fromUtf8("email"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 91, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.exiter = QtGui.QPushButton(self.tab)
        self.exiter.setGeometry(QtCore.QRect(20, 200, 98, 27))
        self.exiter.setObjectName(_fromUtf8("exiter"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Username", None))
        self.label_2.setText(_translate("Dialog", "Enter password", None))
        self.label_3.setText(_translate("Dialog", "Re-enter password", None))
        self.RegisterButton.setText(_translate("Dialog", "Register", None))
        self.label_4.setText(_translate("Dialog", "Email", None))
        self.exiter.setText(_translate("Dialog", "Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Register", None))

