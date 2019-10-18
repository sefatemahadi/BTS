# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from commands import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(925, 597)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 901, 581))
        self.tabWidget.setMinimumSize(QtCore.QSize(901, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 10, 891, 491))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 509, 361, 41))
        self.textEdit.setObjectName("textEdit")
        self.upload_button = QtWidgets.QPushButton(self.tab)
        self.upload_button.setGeometry(QtCore.QRect(370, 510, 121, 41))
        self.upload_button.setObjectName("upload_button")
        self.generate_button = QtWidgets.QPushButton(self.tab)
        self.generate_button.setGeometry(QtCore.QRect(500, 510, 111, 41))
        self.generate_button.setObjectName("generate_button")
        self.delete_button = QtWidgets.QPushButton(self.tab)
        self.delete_button.setGeometry(QtCore.QRect(620, 510, 111, 41))
        self.delete_button.setObjectName("delete_button")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 10, 891, 491))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")

        self.download_button = QtWidgets.QPushButton(self.tab_2)
        self.download_button.setGeometry(QtCore.QRect(740, 510, 151, 41))
        self.download_button.setObjectName("download_button")

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.upload_button.setText(_translate("Dialog", "প্রবন্ধ আপলোড করুন"))
        self.upload_button.clicked.connect(partial(upload_command,Dialog,self.plainTextEdit,self.textEdit))

        self.generate_button.setText(_translate("Dialog", "সারমর্ম তৈরী করুন"))
        self.generate_button.clicked.connect(partial(summarize_command,self.plainTextEdit_2))

        self.delete_button.setText(_translate("Dialog", "মুছে ফেলুন"))
        self.delete_button.clicked.connect(partial(delete_command,self.plainTextEdit,self.textEdit,self.plainTextEdit_2))
        self.download_button.setText(_translate("Dialog", "সারমর্ম ডাউনলোড করুন"))
        self.download_button.clicked.connect(partial(download_command,Dialog))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "প্রবন্ধ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "সারমর্ম"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())