'''
This is the Main GUI Page. This is were the window layout lives.
'''
from tkinter import *
from tkinter import ttk

#Importing own commands
from GraphicalUserInterface.UploadFile import UploadAction
from GraphicalUserInterface.FormatTo import form_to_docx, form_to_wiki, form_to_outline
from GraphicalUserInterface.FormatFrom import form_from_docx, form_from_outline, form_from_wiki
from GraphicalUserInterface.GraphicsVars import *
from run import main
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
def savedoc():
    global path
    print(fileout.get())
    path = desktop + '\\' + fileout.get() + '.docx'
    print(path)
    return path

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_size = str(screen_width) + 'x' + str(screen_height)
root.geometry(screen_size)

root.title('OnTrackNorthAmerica Document Formater')
root.config(background=otnablue, borderwidth=15)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#///// FRAMES /////
mainframe = ttk.Frame(root, padding='15 15 15 15')
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))


fileselect = ttk.Frame(mainframe, padding= '15 15 15 15')
fileselect.grid(column=0, row=0, sticky=(N, S, E, W))
fileselect['borderwidth'] = 5
fileselect['relief'] = 'solid'
fileselect.place(relwidth= 0.6, relheight= 0.25, relx=0.0,rely=0.0)


basic = ttk.Frame(mainframe, padding= '15 15 15 15', width= 250, height= 125)
basic.grid(column=0, row=1, sticky=(N, S, E, W))
basic['borderwidth'] = 5
basic['relief'] = 'solid'
basic.place(relwidth= 0.6, relheight= 0.35, relx=0., rely=0.25)


advanced = ttk.Frame(mainframe, padding= '15 15 15 15', width= 350, height= 150)
advanced.grid(column=0, row=2, sticky=(N, S, E, W))
advanced['borderwidth'] = 5
advanced['relief'] = 'solid'
advanced.place(relwidth= 0.6, relheight= 0.40, rely= 0.60)


preview = ttk.Frame(mainframe, padding= '15 15 15 15', width= 600, height= 300)
preview.grid(column=0, row=1, sticky=(N, S, E, W))
preview['borderwidth'] = 5
preview['relief'] = 'solid'
preview.place(relwidth= 0.4, relheight= 0.90, relx=0.6, rely=0.0)


format = ttk.Frame(mainframe, padding= '15 15 15 15', width= 100, height= 50)
format.grid(column=2, row=2, sticky=(N, S, E, W))
format['borderwidth'] = 5
format['relief'] = 'solid'
format.place(relwidth= 0.4, relheight= 0.10, relx=0.6, rely=0.9)

#///// LAYOUT /////

ttk.Label(fileselect, text='Select and Name your File', font = heading_font).grid(column=0, row=0, sticky=W, pady= 2),
ttk.Label(fileselect, text='Select a File:', font = text_font).grid(column=0, row=1, sticky=W)
ttk.Button(fileselect, text='File', command=UploadAction).grid(column=0, row=1, sticky= W, padx= 100, pady= 2)

fileout = StringVar()
ttk.Label(fileselect, text='Name your file:', font= text_font).grid(column=0, row=2, sticky=W,  pady= 2)
fileout_entry = ttk.Entry(fileselect, width= 15, textvariable=fileout).place(rely= 0.30, relx= 0.08)
ttk.Label(fileselect, text='.docx', font= text_font).place(rely= 0.30, relx= 0.15)
ttk.Button(fileselect, text='Save Doc Name', command=savedoc).grid(column= 2, row=2)
#document type they're formatting to
ttk.Label(basic, text='Basic Formatting Options', font = heading_font, borderwidth= 3, border= 3).grid(column=0, row=0, sticky=W, pady= 10)
ttk.Label(basic, text='What format do you want to Convert your document to?', font = text_font, borderwidth= 3, border= 3).grid(column=0, row=2, sticky=W, pady= 10)
ttk.Button(basic, text='Wiki', command=form_to_wiki).grid(column=0, row=3, sticky=W)
ttk.Button(basic, text='Outline', command=form_to_outline).grid(column=0, row=3, sticky=N)
ttk.Button(basic, text='Word', command=form_to_docx).grid(column=0, row=3, sticky=E)

#document type they're formatting from
ttk.Label(basic, text="What format ws your document Originaly in?", font = text_font).grid(column=0, row=4, sticky=W, pady= 10)
ttk.Button(basic, text='Wiki', command=form_from_wiki).grid(column=0, row=5, sticky=W)
ttk.Button(basic, text='Outline', command=form_from_outline).grid(column=0, row=5, sticky=N)
ttk.Button(basic, text='Word', command=form_from_docx).grid(column=0, row=5, sticky=E)

ttk.Label(advanced, text= 'Advanced Formatting Options', font = heading_font, borderwidth= 3, border= 3).grid(column=0, row=0, sticky=W, pady= 10)
#Make all headings into Decimals
#Make all headings into norm text
#make all headings into Headings

ttk.Label(preview, text='Document Preview will go here', font = heading_font, borderwidth= 3, border= 3).grid(column=0, row=0, sticky=W, pady= 10)

form1 = ttk.Button(format, text='Format', command=main)
form1.place(relx=0.94, rely=0.85)


root.mainloop()