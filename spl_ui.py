# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spl3_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# try:
#     import os
#     import sys
#     import logging
# except Exception as e:
#     print(e)
#
# def _append_run_path():
#     if getattr(sys, 'frozen', False):
#         pathlist = []
#
#         # If the application is run as a bundle, the pyInstaller bootloader
#         # extends the sys module by a flag frozen=True and sets the app
#         # path into variable _MEIPASS'.
#         pathlist.append(sys._MEIPASS)
#
#         # the application exe path
#         _main_app_path = os.path.dirname(sys.executable)
#         pathlist.append(_main_app_path)
#
#         # append to system path enviroment
#         os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist)
#
#     logging.error("current PATH: %s", os.environ['PATH'])
#
# _append_run_path()

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except Exception as e:
    print(e)

try:
    class Ui_Dialog(object):
        def setupUi(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(773, 470)
            Dialog.setStyleSheet("background-image: url(bg1.png);")
            self.line = QtWidgets.QFrame(Dialog)
            self.line.setGeometry(QtCore.QRect(130, 0, 21, 471))
            self.line.setFrameShape(QtWidgets.QFrame.VLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.lineEdit = QtWidgets.QLineEdit(Dialog)
            self.lineEdit.setGeometry(QtCore.QRect(0, 100, 141, 31))
            self.lineEdit.setStyleSheet("boarder:1px solid balck;")
            self.lineEdit.setObjectName("lineEdit")
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.setGeometry(QtCore.QRect(10, 20, 111, 51))
            self.pushButton.setObjectName("pushButton")

            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

        def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.pushButton.setText(_translate("Dialog", "PushButton"))


    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
except Exception as e:
    print(e)
while True:
    continue

