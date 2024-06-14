from tkinter import *
from tkinter import ttk
from GraphicalUserInterface.GraphicsVars import text_font

def savedoc():
    global path
    import os
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    path = desktop + '\\' + fileout.get()
    return path

def saveas():
    formnsave= Toplevel()
    fileout = StringVar()
    ttk.Label(formnsave, text='Name your file:', font= text_font).grid(column=0, row=2, sticky=W,  pady= 2)
    fileout_entry = ttk.Entry(formnsave, width= 15, textvariable=fileout).place(rely= 0.30, relx= 0.08)
    ttk.Label(formnsave, text='.docx', font= text_font).place(rely= 0.30, relx= 0.15)
    ttk.Button(formnsave, text='Save Doc Name', command=savedoc).grid(column= 2, row=2)

