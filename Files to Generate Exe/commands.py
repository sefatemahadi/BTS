from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from generate_summary import generate

file_name =None
dialog =None

def upload_command(object,plain_text_edit,path_edit):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    global file_name
    file_name, _ = QFileDialog.getOpenFileName(object, "প্রবন্ধ নির্বাচন করুন", "",
                                              "All Files (*);;Python Files (*.py)", options=options)
    file =open(file_name)
    plain_text_edit.insertPlainText(file.read())
    file.close()
    path_edit.setText(file_name)
    dialog =object

def delete_command(article_text_edit,path_edit,summary_text_edit):
    article_text_edit.clear()
    path_edit.clear()
    summary_text_edit.clear()
    global file_name
    file_name =None

def summarize_command(plain_text_edit):
    global file_name
    if file_name == None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("প্রবন্ধ নির্বাচন করা হয়নি!")
        msg.exec_()
        return
    generate(file_name)
    file =open('summary.txt')
    plain_text_edit.insertPlainText(file.read())
    file.close()
    QtGui.QToolTip.showText(QtCore.QPoint(100, 200), "INSERTED SUCCESSFULLY", dialog.submitPushButton)

def download_command(object):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    global file_name
    if file_name == None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("প্রবন্ধ নির্বাচন করা হয়নি!")
        msg.exec_()
        return
    dir_name = str(QFileDialog.getExistingDirectory(object, "ডাউনলোড পথ নির্বাচন করুন"))
    downloaded_file =open(dir_name+'/downloaded_summary.txt','w')
    file_name =open('summary.txt','r')
    for line in file_name.readlines():
        downloaded_file.write(line)
    file_name.close()
    downloaded_file.close()
    msg = QMessageBox()
    msg.setText("ডাউনলোড সম্পূর্ণ  হয়েছে")
    msg.exec_()


