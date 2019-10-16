#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Oct 14, 2019 12:21:47 PM +06  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support
from commands import summary,upload,delete

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+328+213")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(relx=0.0, rely=0.022, relheight=0.869
                                 , relwidth=0.985)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="none")

        self.upload_button = tk.Button(top)
        self.upload_button.place(relx=0.083, rely=0.911, height=24, width=67)
        self.upload_button.configure(activebackground="#ececec")
        self.upload_button.configure(activeforeground="#000000")
        self.upload_button.configure(background="#d9d9d9")
        self.upload_button.configure(disabledforeground="#a3a3a3")
        self.upload_button.configure(foreground="#000000")
        self.upload_button.configure(highlightbackground="#d9d9d9")
        self.upload_button.configure(highlightcolor="black")
        self.upload_button.configure(pady="0")
        self.upload_button.configure(text='''Upload''')
        self.upload_button.configure(command =lambda :upload())

        self.summary_button = tk.Button(top)
        self.summary_button.place(relx=0.217, rely=0.911, height=24, width=67)
        self.summary_button.configure(activebackground="#ececec")
        self.summary_button.configure(activeforeground="#000000")
        self.summary_button.configure(background="#d9d9d9")
        self.summary_button.configure(disabledforeground="#a3a3a3")
        self.summary_button.configure(foreground="#000000")
        self.summary_button.configure(highlightbackground="#d9d9d9")
        self.summary_button.configure(highlightcolor="black")
        self.summary_button.configure(pady="0")
        self.summary_button.configure(text='''Summary''')
        self.summary_button.configure(command =lambda :summary(self.Scrolledtext1))

        self.clear_button = tk.Button(top)
        self.clear_button.place(relx=0.358, rely=0.911, height=24, width=67)
        self.clear_button.configure(activebackground="#ececec")
        self.clear_button.configure(activeforeground="#000000")
        self.clear_button.configure(background="#d9d9d9")
        self.clear_button.configure(disabledforeground="#a3a3a3")
        self.clear_button.configure(foreground="#000000")
        self.clear_button.configure(highlightbackground="#d9d9d9")
        self.clear_button.configure(highlightcolor="black")
        self.clear_button.configure(pady="0")
        self.clear_button.configure(text='''Clear''')
        self.clear_button.configure(command =lambda :delete(self.Scrolledtext1))

        # self.Scrolledtext1 = ScrolledText(top)
        # self.Scrolledtext1.place(relx=0.0, rely=0.022, relheight=0.869
        #         , relwidth=0.985)
        # self.Scrolledtext1.configure(background="white")
        # self.Scrolledtext1.configure(font="TkTextFont")
        # self.Scrolledtext1.configure(foreground="black")
        # self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        # self.Scrolledtext1.configure(highlightcolor="black")
        # self.Scrolledtext1.configure(insertbackground="black")
        # self.Scrolledtext1.configure(insertborderwidth="3")
        # self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        # self.Scrolledtext1.configure(selectforeground="black")
        # self.Scrolledtext1.configure(wrap="none")

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





