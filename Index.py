from tkinter import *
from tkinter import ttk
#from run import main
from GraphicalUserInterface.UploadFile import UploadAction
#Custom
from GraphicalUserInterface.FormatTo import form_to_docx, form_to_wiki, form_to_outline
from GraphicalUserInterface.FormatFrom import form_from_docx, form_from_outline, form_from_wiki
from run import main
root = Tk()
root.title('OnTrackNorthAmerica Document Formater')

root.geometry('500x250')
mainframe = ttk.Frame(root, padding ='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Select a File:').grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text='Select a File', command=UploadAction).grid(column=1, row=2, sticky=W)
#document type they're formatting to
#if they select formatting to first give them a popup telling them to select format from first
ttk.Label(mainframe, text='What Document Type are you formating to?').grid(column=1, row=5, sticky=W)

ttk.Button(mainframe, text='Wiki', command=form_to_wiki).grid(column=1, row=6, sticky=W)
ttk.Button(mainframe, text='Outline', command=form_to_outline).grid(column=1, row=6, sticky=E)
ttk.Button(mainframe, text='Word Document(Docx)', command=form_to_docx).grid(column=3, row=6, sticky=W)

ttk.Button(mainframe, text='Format', command=main).grid(column=12, row=12, sticky=S)

#document type they're formatting from
ttk.Label(mainframe, text='What Document Type are you Formatting From?').grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text='Wiki', command=form_from_wiki).grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text='Outline', command=form_from_outline).grid(column=1, row=4, sticky=E)
ttk.Button(mainframe, text='Word Document(Docx)', command=form_from_docx).grid(column=3, row=4, sticky=W)


'''
ttk.Button(mainframe, text='Advanced', command=).grid(column=1, row=1, sticky=E)
ttk.Button(mainframe, text='Basic', command=).grid(column=3, row=3, sticky=E)
'''
root.mainloop()