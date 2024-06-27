'''
This is the Main GUI Page. This is were the window layout lives.
'''
##############################################################################
'''
Imports
'''
from tkinter import *
from tkinter import ttk

#Importing own commands
from GraphicalUserInterface.UploadFile import UploadAction

from GraphicalUserInterface.FormatTo import form_to_docx, form_to_wiki, form_to_outline
from GraphicalUserInterface.FormatFrom import form_from_docx, form_from_outline, form_from_wiki
from GraphicalUserInterface.GraphicsVars import *
from run import main

'''
Functions
'''

###############################################################################
'''
WINDOWS AND FRAMES BEGIN
'''
root = Tk()
root.resizable(0,0)
root.geometry('600x400')

root.title('OnTrackNorthAmerica Document Formater')
root.config(background=otnablue, borderwidth=10)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#///// FRAMES /////
mainframe = ttk.Frame(root, padding='2 2 2 2')
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))


fileselect = ttk.Frame(mainframe, padding= '2 2 2 2')
fileselect.grid(column=0, row=0, sticky=(N, S, E, W))
fileselect['borderwidth'] = 5
fileselect['relief'] = 'solid'
fileselect.place(relwidth= 1.0, relheight= 0.25, relx=0.0,rely=0.0)


basic = ttk.Frame(mainframe, padding= '2 2 2 2')
basic.grid(column=0, row=1, sticky=(N, S, E, W))
basic['borderwidth'] = 5
basic['relief'] = 'solid'
basic.place(relwidth= 1.0, relheight= 0.35, relx=0., rely=0.25)


advanced = ttk.Frame(mainframe, padding= '2 2 2 2')
advanced.grid(column=0, row=2, sticky=(N, S, E, W))
advanced['borderwidth'] = 5
advanced['relief'] = 'solid'
advanced.place(relwidth= 1.0, relheight= 0.40, rely= 0.60)


format = ttk.Frame(mainframe, padding= '2 2 2 2')
format.grid(column=2, row=2, sticky=(N, S, E, W))
format['borderwidth'] = 5
format['relief'] = 'solid'
format.place(relwidth= 0.15, relheight= 0.08, relx=0.85, rely=0.912)
'''
WINDOWS AND FRAMES END
'''
###############################################################################
layout = [
    ttk.Label(fileselect, text='Select and Name your File').grid(column=0, row=0, sticky=W),
    ttk.Label(fileselect, text='Select a File:').grid(column=0, row=1, sticky=W),
    ttk.Button(fileselect, text='File', command=UploadAction).grid(column=0, row=1, sticky= W, padx= 100),

    #document type they're formatting to
    ttk.Label(basic, text='Basic Formatting Options').grid(column=0, row=0, sticky=W),
    ttk.Label(basic, text='What format do you want to Convert your document to?').grid(column=0, row=2, sticky=W),
    ttk.Button(basic, text='Wiki', command=form_to_wiki).grid(column=0, row=3, sticky=W),
    ttk.Button(basic, text='Outline', command=form_to_outline).grid(column=0, row=3, sticky=N),
    ttk.Button(basic, text='Word', command=form_to_docx).grid(column=0, row=3, sticky=E),

    #document type they're formatting from
    ttk.Label(basic, text="What format ws your document Originaly in?").grid(column=0, row=4, sticky=W),
    ttk.Button(basic, text='Wiki', command=form_from_wiki).grid(column=0, row=5, sticky=W),
    ttk.Button(basic, text='Outline', command=form_from_outline).grid(column=0, row=5, sticky=N),
    ttk.Button(basic, text='Word', command=form_from_docx).grid(column=0, row=5, sticky=E),

    ttk.Label(advanced, text= 'Advanced Formatting Options', border= 3).grid(column=0, row=0, sticky=W),
]

#layout features that can't be containes in an array
form1 = ttk.Button(format, text='Save File', command=main).grid(column=0, row=0)
root.mainloop()