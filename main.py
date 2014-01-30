# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Jan 30 22:26:40 2014
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
        Dialog.resize(400, 302)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 341))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.Filename = QtGui.QLineEdit(self.tab)
        self.Filename.setGeometry(QtCore.QRect(40, 20, 271, 27))
        self.Filename.setObjectName(_fromUtf8("Filename"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(320, 20, 71, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.userBox = QtGui.QComboBox(self.tab)
        self.userBox.setGeometry(QtCore.QRect(40, 50, 271, 31))
        self.userBox.setObjectName(_fromUtf8("userBox"))
        self.sendButton = QtGui.QPushButton(self.tab)
        self.sendButton.setGeometry(QtCore.QRect(320, 50, 71, 27))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.listView = QtGui.QListView(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(0, 0, 401, 231))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.getFile = QtGui.QPushButton(self.tab_2)
        self.getFile.setGeometry(QtCore.QRect(290, 240, 98, 27))
        self.getFile.setObjectName(_fromUtf8("getFile"))
        self.exiter = QtGui.QPushButton(self.tab_2)
        self.exiter.setGeometry(QtCore.QRect(10, 240, 98, 27))
        self.exiter.setObjectName(_fromUtf8("exiter"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Open", None))
        self.label.setText(_translate("Dialog", "File", None))
        self.label_2.setText(_translate("Dialog", "User", None))
        self.sendButton.setText(_translate("Dialog", "Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Send", None))
        self.getFile.setText(_translate("Dialog", "Get", None))
        self.exiter.setText(_translate("Dialog", "Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Receive", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "My Files", None))

