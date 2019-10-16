from tkinter import *
from tkinter import filedialog
from generate_summary import generate

import os

path =str(os.getcwd())

def upload():
    global path
    path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",filetypes=(("txt files", "*.txt"),("all files", "*.*")))

def summary(object):
    global path
    output_file =generate(path)
    lines =open(output_file,'r',encoding='utf-8').readlines()
    # strings =''
    # for line in lines:
    #     strings =strings+line
    # object.insert(END,strings)
    # # print(path)
    # # print(object)
    for i in range(len(lines)):
        # Label(object,text =lines[i]).grid(row=i,column=0)
        Label(object, text=lines[i], anchor='w').pack(fill='both')
def delete(object):
    object.delete('1.0', END)
