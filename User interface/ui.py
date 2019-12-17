# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from commands import *
from functools import partial

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1025, 582)
        self.Tabs = QtWidgets.QTabWidget(Dialog)
        self.Tabs.setGeometry(QtCore.QRect(0, 0, 1021, 581))
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
        self.articleBrowser.setGeometry(QtCore.QRect(0, 10, 1001, 491))
        self.articleBrowser.setObjectName("articleBrowser")
        self.summarizeButton = QtWidgets.QPushButton(self.articleTab)
        self.summarizeButton.setGeometry(QtCore.QRect(150, 510, 141, 41))
        self.summarizeButton.setObjectName("summarizeButton")
        self.deleteButton = QtWidgets.QPushButton(self.articleTab)
        self.deleteButton.setGeometry(QtCore.QRect(300, 510, 141, 41))
        self.deleteButton.setObjectName("deleteButton")
        self.tab1Highlight = QtWidgets.QRadioButton(self.articleTab)
        self.tab1Highlight.setGeometry(QtCore.QRect(450, 520, 81, 23))
        self.tab1Highlight.setObjectName("tab1Highlight")
        self.tab2Highlight = QtWidgets.QRadioButton(self.articleTab)
        self.tab2Highlight.setGeometry(QtCore.QRect(550, 520, 81, 23))
        self.tab2Highlight.setObjectName("tab2Highlight")
        self.highlightLabel = QtWidgets.QLabel(self.articleTab)
        self.highlightLabel.setGeometry(QtCore.QRect(450, 500, 211, 17))
        self.highlightLabel.setObjectName("highlightLabel")
        self.restoreMainArticle = QtWidgets.QRadioButton(self.articleTab)
        self.restoreMainArticle.setGeometry(QtCore.QRect(670, 520, 111, 23))
        self.restoreMainArticle.setObjectName("restoreMainArticle")
        self.multiple_summary = QtWidgets.QPushButton(self.articleTab)
        self.multiple_summary.setGeometry(QtCore.QRect(860, 510, 141, 41))
        self.multiple_summary.setObjectName("multiple_summary")
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
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # self.Tabs.setTabText(self.Tabs.indexOf(self.instructionTab), _translate("Dialog", "Page"))
        # self.uploadButton.setText(_translate("Dialog", "Upload file"))
        # self.summarizeButton.setText(_translate("Dialog", "Upload file"))
        # self.deleteButton.setText(_translate("Dialog", "Upload file"))
        # self.tab1Highlight.setText(_translate("Dialog", "RadioButton"))
        # self.tab2Highlight.setText(_translate("Dialog", "RadioButton"))
        # self.highlightLabel.setText(_translate("Dialog", "TextLabel"))
        # self.restoreMainArticle.setText(_translate("Dialog", "RadioButton"))
        self.multiple_summary.setText(_translate("Dialog", "একাধিক প্রবন্ধ"))
        # self.Tabs.setTabText(self.Tabs.indexOf(self.articleTab), _translate("Dialog", "Tab 1"))
        # self.tab1Download.setText(_translate("Dialog", "Upload file"))
        # self.Tabs.setTabText(self.Tabs.indexOf(self.pageTab), _translate("Dialog", "Tab 2"))
        # self.tab2Download.setText(_translate("Dialog", "Upload file"))
        # self.Tabs.setTabText(self.Tabs.indexOf(self.nopageTab), _translate("Dialog", "Page"))

        self.Tabs.setTabText(self.Tabs.indexOf(self.instructionTab), _translate("Dialog", "নির্দেশনাবলী"))
        self.uploadButton.setText(_translate("Dialog", "প্রবন্ধ আপলোড"))
        self.summarizeButton.setText(_translate("Dialog", "সারমর্ম তৈরী"))
        self.deleteButton.setText(_translate("Dialog", "প্রবন্ধ মুছে ফেলুন"))
        self.highlightLabel.setText(_translate("Dialog", "হাইলাইট:"))
        self.tab1Highlight.setText(_translate("Dialog", "সারমর্ম ১"))
        self.tab2Highlight.setText(_translate("Dialog", "সারমর্ম ২"))
        self.restoreMainArticle.setText(_translate("Dialog", "পুনঃস্থাপন"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.articleTab), _translate("Dialog", "প্রবন্ধ"))
        self.tab1Download.setText(_translate("Dialog", "ডাউনলোড"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.pageTab), _translate("Dialog", "সারমর্ম ১ (উপ-প্রবন্ধ পদ্ধতি)"))
        self.tab2Download.setText(_translate("Dialog", "ডাউনলোড"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.nopageTab), _translate("Dialog", "সারমর্ম ২ (প্রচলিত পদ্ধতি)"))

        # self.instructionBrowser.setText(open('instructions.txt', 'r', encoding='utf-8').read())
        self.instructionBrowser.setText(
            'সফটওয়্যার টি ব্যবহার করার আগে নিচের নির্দেশনাবলী সমূহ পড়ার জন্য বিশেষভাবে অনুরোধ করা হলো:\n\n১) এই সফটওয়্যারটি বাংলা প্রবন্ধ বা খবর এর গুরুত্বপূর্ণ  বাক্য সমূহ নির্বাচন করার মাধ্যমে সারমর্ম তৈরী করে\n\n২) ন্যাচারাল ল্যাংগুয়েজ প্রসেসিং কমিউনিটি তে স্বয়ংক্রিয় সারমর্ম প্রস্তুতির ক্ষেত্রে মূল প্রবন্ধ এর এক তৃতীয়াংশ তুলে ধরাটা স্ট্যান্ডার্ড বিধায় এক্ষেত্রেও সারমর্ম এর দৈর্ঘ  মূল প্রবন্ধ এর এক তৃতীয়াংশ হবে\n\n৩) সারমর্ম তৈরী করার দুইটি উপায় হলো:\n\n\t১) প্রচলিত পদ্ধতি: সমগ্র  প্রবন্ধ থেকে গুরুত্বপূর্ণ  বাক্য সমূহ তুলে আনার মাধ্যমে\n\n\t২) উপ-প্রবন্ধ পদ্ধতি: পুরো প্রবন্ধ কে কয়েকটি চলমান উপ প্রবন্ধে ভাগ করে প্রত্যেক উপ প্রবন্ধ এর সবচেয়ে গুরুত্বপূর্ণ বাক্য নির্বাচন করার মাধ্যমে (প্রত্যেক উপ প্রবন্ধের দৈর্ঘ মূল প্রবন্ধ এর এক তৃতীয়াংশ)\n\n৪) সারমর্ম তৈরী করার জন্য পরবর্ত্তী ট্যাব এর "প্রবন্ধ আপলোড করুন" বাটন এ ক্লিক করুন এবং প্রবন্ধ এর পাথ নির্বাচন করুন\n\n৫) টেক্সট ফাইল থেকে প্রবন্ধ নির্বাচন এর বেলায় সতর্ক থাকুন যেন একটি বাক্য দুইটি আলাদা লাইন এ না থাকে\n\n৬)  সারমর্ম তৈরী করার জন্য "সারমর্ম তৈরী করুন" বাটন টিতে ক্লিক করুন\n\n৭) "সারমর্ম ১" ট্যাব টিতে উপ-প্রবন্ধ পদ্ধতিতে এবং "সারমর্ম ২" ট্যাব টিতে প্রচলিত পদ্ধতিতে তৈরী করা সারমর্ম তুলে ধরা হবে\n\n৮) নতুন প্রবন্ধ এর সারমর্ম তৈরী করার জন্য "প্রবন্ধ মুছে ফেলুন" বাটন টিতে ক্লিক করুন\n\n৯) তৈরিকৃত সারমর্ম ডাউনলোড করার জন্য "ডাউনলোড করুন" বাটন টিতে ক্লিক করুন এবং পাথ নির্বাচন করুন\n\n১০) মূল প্রবন্ধ এর মধ্য ১ নং সারমর্ম কে হাইলাইট করতে চাইলে "সারমর্ম ১" রেডিও বাটন টিতে ক্লিক করুন, ২ নং সারমর্ম হাইলাইট করতে চাইলে "সারমর্ম ২" বাটন টিতে ক্লিক করুন, মূল প্রবন্ধ পুনঃস্থাপন করতে চাইলে  "মূল প্রবন্ধ পুনঃস্থাপন করুন" রেডিও বাটন টিতে ক্লিক করুন')
        self.uploadButton.clicked.connect(partial(upload, dialog, self.articleBrowser))
        self.deleteButton.clicked.connect(partial(delete, self.articleBrowser, self.pageBrowser, self.nonpageBrowser))
        self.summarizeButton.clicked.connect(partial(summarize, self.pageBrowser, self.nonpageBrowser))
        self.tab1Download.clicked.connect(partial(download, dialog, True))
        self.tab2Download.clicked.connect(partial(download, dialog, False))
        self.tab1Highlight.toggled.connect(
            partial(radio_action, self.articleBrowser, self.tab1Highlight, self.tab2Highlight))
        self.tab2Highlight.toggled.connect(
            partial(radio_action, self.articleBrowser, self.tab1Highlight, self.tab2Highlight))
        self.restoreMainArticle.toggled.connect(partial(restore, self.articleBrowser))
        self.multiple_summary.clicked.connect(partial(multiple,dialog))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
