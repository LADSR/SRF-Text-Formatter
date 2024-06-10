'''
This is where i test and debug functions that aren't working
A good method is to print the paragraph or run's text and go from there
'''
from tkinter import *
from tkinter import ttk
import os

root = Tk()

file = StringVar()
file_ent= ttk.Entry(root, width= 15, textvariable=file)
file_ent.pack()

def onclick():
    global name
    file.trace
    ("w", lambda *args: file.get(), interval=0.2)
    print (name)
    return name
go = ttk.Button(root, text='GO', command=onclick)
go.pack()

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

print(desktop)
root.mainloop()
