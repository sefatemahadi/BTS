import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from PyQt5.QtWidgets import QFileDialog, QMessageBox
from summary import Generate

file_name =None
dialog =None

def upload(object,article_browser):
    #print(object,plain_text_edit,path_edit)
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    global file_name
    file_name, _ = QFileDialog.getOpenFileName(object, "প্রবন্ধ নির্বাচন করুন", "","All Files (*);;Python Files (*.py)", options=options)
    file =open(file_name,'r',encoding='utf-8')
    lines =file.readlines()
    article =''
    for line in lines:
        line =line[:len(line)-1]
        article+=line
    article_browser.setText(article)
    file.close()

def delete(article_browser,page_browser,non_page_browser):
    article_browser.clear()
    page_browser.clear()
    non_page_browser.clear()
    global file_name
    file_name =None
#lines[i] ='<span style=\" color: #f5f5f0;\">'+lines[i]+'</span>'
def mark_lines(article_browser,lines,indexes):
    article =''
    for i in range(len(lines)):
        line =lines[i]
        if i not in indexes:
            line =line[:len(line)-1]
            line='<span style=\" color: #ccccb3;\">'+line+'</span>'
        article+=line
    article_browser.setHtml(article)

def summarize(page_browser,non_page_browser):
    global file_name
    if file_name == None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("প্রবন্ধ নির্বাচন করা হয়নি!")
        msg.exec_()
        return
    Generate(file_name,3)

    indexes1 =open('page_summary.txt','r').readlines()
    for i in range(len(indexes1)):
        indexes1[i] =int(indexes1[i])

    lines =open(file_name,'r').readlines()
    line =''
    for i in indexes1:
        lines[i] =lines[i][:len(lines[i])]
        line+=lines[i]
    page_browser.setText(line)

    indexes2 =open('trad_summary.txt').readlines()
    for i in range(len(indexes2)):
        indexes2[i] =int(indexes2[i])

    line = ''
    for i in indexes2:
        lines[i] =lines[i][:len(lines[i])]
        line += lines[i]
    non_page_browser.setText(line)

    msg = QMessageBox()
    msg.setText("সারমর্ম তৈরী সম্পূর্ণ হয়েছে")
    msg.exec_()

def download(object,download_type):
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


    indexes = open('page_summary.txt', 'r').readlines()
    if download_type == False:
        indexes =open('trad_summary.txt').readlines()

    for i in range(len(indexes)):
        indexes[i] =int(indexes[i])
    lines =open(file_name,'r').readlines()

    for index in indexes:
        downloaded_file.write(lines[index])
    downloaded_file.close()
    msg = QMessageBox()
    msg.setText("ডাউনলোড সম্পূর্ণ  হয়েছে")
    msg.exec_()

def radio_action(article_browser,tab1,tab2):
    lines = open(file_name, 'r').readlines()
    article_browser.clear()

    if tab1.isChecked():
        indexes1 = open('page_summary.txt', 'r').readlines()
        for i in range(len(indexes1)):
            indexes1[i] = int(indexes1[i])

        mark_lines(article_browser,lines,indexes1)

    elif tab2.isChecked():
        indexes1 = open('trad_summary.txt', 'r').readlines()
        for i in range(len(indexes1)):
            indexes1[i] = int(indexes1[i])

        mark_lines(article_browser, lines, indexes1)

def restore_main_article(article_browser):
    if file_name == None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("প্রবন্ধ নির্বাচন করা হয়নি!")
        msg.exec_()
        return
    article_browser.clear()
    file =open(file_name,'r',encoding='utf-8')
    lines =file.readlines()
    article =''
    for line in lines:
        line =line[:len(line)-1]
        article+=line
    file.close()
    article_browser.setText(article)