from tkinter import *
from tkinter import messagebox
import os
import os.path
import webbrowser

path, name = "", ""


def authentication():
    root = Tk()
    root.title("Authentication")
    root.minsize(width=400, height=300)

    getName = Entry(root, width=25)
    getName.insert(0, "NAME")
    getName.pack(ipady=5, pady=10)

    getPassword = Entry(root, width=25)
    getPassword.insert(0, "PASSWORD")
    getPassword.pack(ipady=5, pady=10)

    def nameEvent(event):
        getName.delete(0, 'end')

    getName.bind('<Button-1>', nameEvent)

    def passwordEvent(event):
        getPassword.delete(0, 'end')

    getPassword.bind('<Button-1>', passwordEvent)

    def enterAction():
        global path
        global name
        name = getName.get()
        password = getPassword.get()
        fp = open("data.txt", "r")
        n, flag = int(fp.readline()), 0
        for i in range(n):
            n = fp.readline()
            p = fp.readline()
            if n.strip("\n") == name and p.strip('\n') == password:
                # print (i)
                fp.close()
                path = "/home/sand_boa/" + name
                root.destroy()
                flag = 1
        if not flag:
            messagebox.showinfo("test", "Not found")
        fp.close()

    Button(root, text="Enter", command=enterAction, width=22).pack(ipady=5, pady=10)

    def registerAction():
        name = getName.get()
        password = getPassword.get()
        fp = open("data.txt", "r")
        n = int(fp.readline())
        names, passwords = [], []
        for i in range(n):
            a = fp.readline()
            b = fp.readline()
            names.append(a.strip())
            passwords.append(b.strip())
        fp.close()
        fp = open("data.txt", "w")
        fp.write(str(n + 1) + "\n")
        for i in range(n):
            fp.write(names[i] + "\n")
            fp.write(passwords[i] + "\n")
        fp.write(name + "\n")
        fp.write(password + "\n")
        fp.close()
        os.mkdir("/home/sand_boa/" + name)
        os.mkdir("/home/sand_boa/" + name + "/Desktop")
        os.mkdir("/home/sand_boa/" + name + "/Downloads")
        os.mkdir("/home/sand_boa/" + name + "/Documents")
        messagebox.showinfo("test", "Registration Done.Now enter into the system")

    Button(root, text="register", command=registerAction, width=22).pack(ipady=5, pady=10)

    root.mainloop()


authentication()

root = Tk()
upwin = Frame(root, width=800, height=50)
upwin.pack(expand=False)
sidewin = Frame(root, background="green", width=150, height=370)
sidewin.pack(expand=False, side='left')
dirwin = Frame(root, background="yellow", width=700, height=370)
dirwin.pack(expand=False, side='left')
dir_icon = PhotoImage(file="dir.png")

dhcor, dvcor = 0, 0
nhcor, nvcor = 0, 40


def action(string, isdir):
    global path

    if (isdir == 0):
        path += "/" + string
        decorate(os.listdir(path))
        return
    cpath = path + "/" + string
    webbrowser.open(cpath)


rmenu = Menu(root, tearoff=0)
bmenu = Menu(root, tearoff=0)


def runbind(event):
    root.unbind("<Button-3>")


def rbind(event):
    root.bind("<Button-3>", rpost)


def bpost(event):
    bmenu.post(event.x_root, event.y_root)


def decorate(dirname):
    global dirwin
    global dir_icon
    global root

    for d in dirwin.winfo_children():
        d.destroy()

    root.title(path[10:len(path)])
    dhcor, dvcor = 0, 0
    nhcor, nvcor = 0, 40

    bmenu.add_radiobutton(label="rename")
    bmenu.add_radiobutton(label="move")
    bmenu.add_radiobutton(label="share")
    bmenu.add_radiobutton(label="remove")

    dirarr = []
    for i in range(len(dirname)):
        if (os.path.isdir(os.path.join(path, dirname[i]))):
            dirarr.append(Button(dirwin, text=dirname[i], image=dir_icon, command=lambda i=i: action(dirname[i], 0)))
            dirarr[i].image = dir_icon
        else:
            dirarr.append(Button(dirwin, text=dirname[i], command=lambda i=i: action(dirname[i], 1)))
        dirarr[i].place(x=dhcor, y=dvcor)
        Label(dirwin, text=dirname[i]).place(x=nhcor, y=nvcor)
        dirarr[i].bind('<Enter>', runbind)
        dirarr[i].bind('<Leave>', rbind)
        dirarr[i].bind('<Button-3>', bpost)
        dhcor += 80
        nhcor += 80


def rpost(event):
    rmenu.post(event.x_root, event.y_root)


'''
def f():
	dname =""
	a =Tk()
	e =Entry(a)
	e.pack()

	def g():
		global dname
		dname =e.get()
		a.destroy()

	b =Button(a,text ="Create",command =g)
	b.pack()
	a.mainloop()
	return dname
'''


def createDir():
    e = Entry(sidewin)
    e.place(x=0, y=200)

    def a(ob):
        string = e.get()
        e.destroy()
        ob.destroy()
        cpath = path + "/" + string
        os.mkdir(cpath)
        decorate(os.listdir(path))

    cd = Button(sidewin, text="Create", command=lambda: a(cd))
    cd.place(x=0, y=220)


# print (string)

def cerateDocument():
    e = Entry(sidewin)
    e.place(x=0, y=200)

    def a(ob):
        string = e.get()
        e.destroy()
        ob.destroy()
        cpath = path + "/" + string
        fp = open(cpath, "w")
        decorate(os.listdir(path))

    cd = Button(sidewin, text="Create", command=lambda: a(cd))
    cd.place(x=0, y=220)


def searchEvent(event, entry):
    searchKey = entry.get()
    searchKey = searchKey.lower()
    dirname = []
    for sd in os.listdir(path):
        sd = sd.lower()
        if (sd == searchKey or searchKey in sd):
            dirname.append(sd)
    decorate(dirname)


def side_action(string, isprevious):
    global path
    global name

    if (isprevious):
        path = path[:path.rindex('/')]
        decorate(os.listdir(path))
        return

    path = "/home/sand_boa/" + name + "/" + string
    decorate(os.listdir(path))


def main():
    root.minsize(width=800, height=400)
    root.title("Home")

    rmenu.add_radiobutton(label="Create Directory", command=createDir)
    rmenu.add_radiobutton(label="Create Document", command=cerateDocument)

    root.bind("<Button-3>", rpost)

    decorate(os.listdir(path))

    searchEntry = Entry(upwin)
    searchEntry.insert(0, 'search')
    searchEntry.pack(ipady=5)

    def e(event):
        searchEntry.delete(0, 'end')

    searchEntry.bind('<Button-1>', e)
    searchEntry.bind("<Return>", lambda event: searchEvent(event, searchEntry))

    home = Button(sidewin, text="HOME", width=10, command=lambda: side_action("", 0))
    home.place(x=0, y=0)

    desktop = Button(sidewin, text="DESKTOP", width=10, command=lambda: side_action("Desktop", 0))
    desktop.place(x=0, y=40)

    documents = Button(sidewin, text="DOCUMENTS", width=10, command=lambda: side_action("Documents", 0))
    documents.place(x=0, y=80)

    downloads = Button(sidewin, text="DOWNLOADS", width=10, command=lambda: side_action("Downloads", 0))
    downloads.place(x=0, y=120)

    previous = Button(sidewin, text="PREVIOUS", width=10, command=lambda: side_action("Desktop", 1))
    previous.place(x=0, y=160)

    root.mainloop()


main()