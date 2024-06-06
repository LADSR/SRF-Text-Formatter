'''
This is the Main GUI Page. This is where the Window gets its formatting from.
'''
from tkinter import *
from tkinter import ttk
#from run import main
from GraphicalUserInterface.UploadFile import UploadAction
#Custom
from GraphicalUserInterface.FormatTo import form_to_docx, form_to_wiki, form_to_outline
from GraphicalUserInterface.FormatFrom import form_from_docx, form_from_outline, form_from_wiki
from run import main
from GraphicalUserInterface.GraphicsVars import *

#Root Frame; All other frames and content are nested in this window
root = Tk()
root.title('OnTrackNorthAmerica Document Formater')
root.geometry('750x375')
root.config(background=otnablue, borderwidth=10)

#Mainframe; most content goes in this window
mainframe = ttk.Frame(root, padding='15 15 15 15')
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

layout = [
    ttk.Label(mainframe, text='Select a File:', font = text_font).grid(column=1, row=1, sticky=W),
    ttk.Button(mainframe, text='File', command=UploadAction).grid(column=1, row=1, sticky=E),

    #document type they're formatting to
    ttk.Label(mainframe, text='What Format do you want your document in?', font = text_font).grid(column=1, row=2, sticky=W),

    ttk.Button(mainframe, text='Wiki', command=form_to_wiki).grid(column=1, row=3, sticky=W),
    ttk.Button(mainframe, text='Outline', command=form_to_outline).grid(column=2, row=3, sticky=E),
    ttk.Button(mainframe, text='Word', command=form_to_docx).grid(column=3, row=3, sticky=W),

    #document type they're formatting from
    ttk.Label(mainframe, text="What is Your Document's original format?", font = text_font).grid(column=1, row=4, sticky=W),

    ttk.Button(mainframe, text='Wiki', command=form_from_wiki).grid(column=1, row=5, sticky=W),
    ttk.Button(mainframe, text='Outline', command=form_from_outline).grid(column=2, row=5, sticky=E),
    ttk.Button(mainframe, text='Word', command=form_from_docx).grid(column=3, row=5, sticky=W),

    #Run Formatting Process
    ttk.Button(mainframe, text='Format', command=main).grid(column=12, row=12, sticky=S)
]


'''
#Eventually will open up advance options for more dynamic styling choices
ttk.Button(mainframe, text='Advanced', command=).grid(column=1, row=1, sticky=E)
ttk.Button(mainframe, text='Basic', command=).grid(column=3, row=3, sticky=E)
'''
root.mainloop()