# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import *
from commands3 import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(956, 582)
        self.Tabs = QtWidgets.QTabWidget(Dialog)
        self.Tabs.setGeometry(QtCore.QRect(0, 0, 951, 581))
        self.Tabs.setMinimumSize(QtCore.QSize(901, 0))
        self.Tabs.setObjectName("Tabs")
        self.instructionTab = QtWidgets.QWidget()
        self.instructionTab.setObjectName("instructionTab")
        self.instructionBrowser = QtWidgets.QTextBrowser(self.instructionTab)
        self.instructionBrowser.setGeometry(QtCore.QRect(0, 0, 951, 551))
        self.instructionBrowser.setObjectName("instructionBrowser")
        self.Tabs.addTab(self.instructionTab, "")
        self.articleTab = QtWidgets.QWidget()
        self.articleTab.setObjectName("articleTab")
        self.uploadButton = QtWidgets.QPushButton(self.articleTab)
        self.uploadButton.setGeometry(QtCore.QRect(0, 510, 141, 41))
        self.uploadButton.setObjectName("uploadButton")
        self.articleBrowser = QtWidgets.QTextBrowser(self.articleTab)
        self.articleBrowser.setGeometry(QtCore.QRect(0, 10, 941, 491))
        self.articleBrowser.setObjectName("articleBrowser")
        self.summarizeButton = QtWidgets.QPushButton(self.articleTab)
        self.summarizeButton.setGeometry(QtCore.QRect(150, 510, 141, 41))
        self.summarizeButton.setObjectName("summarizeButton")
        self.deleteButton = QtWidgets.QPushButton(self.articleTab)
        self.deleteButton.setGeometry(QtCore.QRect(300, 510, 141, 41))
        self.deleteButton.setObjectName("deleteButton")
        self.tab1Highlight = QtWidgets.QRadioButton(self.articleTab)
        self.tab1Highlight.setGeometry(QtCore.QRect(450, 520, 111, 23))
        self.tab1Highlight.setObjectName("tab1Highlight")
        self.tab2Highlight = QtWidgets.QRadioButton(self.articleTab)
        self.tab2Highlight.setGeometry(QtCore.QRect(570, 520, 111, 23))
        self.tab2Highlight.setObjectName("tab2Highlight")
        self.highlightLabel = QtWidgets.QLabel(self.articleTab)
        self.highlightLabel.setGeometry(QtCore.QRect(450, 500, 211, 17))
        self.highlightLabel.setObjectName("highlightLabel")
        self.restoreMainArticle = QtWidgets.QRadioButton(self.articleTab)
        self.restoreMainArticle.setGeometry(QtCore.QRect(690, 520, 191, 23))
        self.restoreMainArticle.setObjectName("restoreMainArticle")
        self.Tabs.addTab(self.articleTab, "")
        self.pageTab = QtWidgets.QWidget()
        self.pageTab.setObjectName("pageTab")
        self.tab1Download = QtWidgets.QPushButton(self.pageTab)
        self.tab1Download.setGeometry(QtCore.QRect(800, 510, 141, 41))
        self.tab1Download.setObjectName("tab1Download")
        self.pageBrowser = QtWidgets.QTextBrowser(self.pageTab)
        self.pageBrowser.setGeometry(QtCore.QRect(0, 10, 941, 491))
        self.pageBrowser.setObjectName("pageBrowser")
        self.Tabs.addTab(self.pageTab, "")
        self.nopageTab = QtWidgets.QWidget()
        self.nopageTab.setObjectName("nopageTab")
        self.tab2Download = QtWidgets.QPushButton(self.nopageTab)
        self.tab2Download.setGeometry(QtCore.QRect(800, 510, 141, 41))
        self.tab2Download.setObjectName("tab2Download")
        self.nonpageBrowser = QtWidgets.QTextBrowser(self.nopageTab)
        self.nonpageBrowser.setGeometry(QtCore.QRect(0, 10, 941, 491))
        self.nonpageBrowser.setObjectName("nonpageBrowser")
        self.Tabs.addTab(self.nopageTab, "")

        self.retranslateUi(Dialog)
        self.Tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "বাংলা সারমর্ম"))

        self.Tabs.setTabText(self.Tabs.indexOf(self.instructionTab), _translate("Dialog", "নির্দেশনাবলী"))
        self.uploadButton.setText(_translate("Dialog", "প্রবন্ধ আপলোড করুন"))
        self.summarizeButton.setText(_translate("Dialog", "সারমর্ম তৈরী করুন"))
        self.deleteButton.setText(_translate("Dialog", "প্রবন্ধ মুছে ফেলুন"))
        self.highlightLabel.setText(_translate("Dialog","হাইলাইট করুন:"))
        self.tab1Highlight.setText(_translate("Dialog", "সারমর্ম ১"))
        self.tab2Highlight.setText(_translate("Dialog", "সারমর্ম ২"))
        self.restoreMainArticle.setText(_translate("Dialog", "মূল প্রবন্ধ পুনঃস্থাপন করুন"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.articleTab), _translate("Dialog", "প্রবন্ধ"))
        self.tab1Download.setText(_translate("Dialog", "ডাউনলোড করুন"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.pageTab), _translate("Dialog", "সারমর্ম ১ (উপ-প্রবন্ধ পদ্ধতি)"))
        self.tab2Download.setText(_translate("Dialog", "ডাউনলোড করুন"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.nopageTab), _translate("Dialog", "সারমর্ম ২ (প্রচলিত পদ্ধতি)"))

        self.instructionBrowser.setText(open('instructions.txt', 'r', encoding='utf-8').read())
        self.uploadButton.clicked.connect(partial(upload, dialog, self.articleBrowser))
        self.deleteButton.clicked.connect(partial(delete, self.articleBrowser, self.pageBrowser, self.nonpageBrowser))
        self.summarizeButton.clicked.connect(partial(summarize, self.pageBrowser, self.nonpageBrowser))
        self.tab1Download.clicked.connect(partial(download, dialog, True))
        self.tab2Download.clicked.connect(partial(download, dialog, False))
        self.tab1Highlight.toggled.connect(partial(radio_action, self.articleBrowser, self.tab1Highlight, self.tab2Highlight))
        self.tab2Highlight.toggled.connect(partial(radio_action, self.articleBrowser, self.tab1Highlight, self.tab2Highlight))
        self.restoreMainArticle.toggled.connect(partial(restore_main_article,self.articleBrowser))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
