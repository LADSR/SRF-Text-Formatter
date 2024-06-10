#python docx
from docx import Document
from docx.shared import Pt
#tkinter
from tkinter import *
from tkinter import ttk
#gets user's desktop
import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#custom
#NEEDS DOC FOR DOC SAVE

def main():
    from GraphicalUserInterface.UploadFile import doc
    from GraphicalUserInterface.FormatTo import a
    from Index import fileout
    if a == True:
        from wiki.main import wiki_format
        wiki_format()
        #NOTE: allow people to customize file name
        #Maybe default could be old file name.
        name = str(fileout.get)
        doc.save(desktop + 'wiki_out.docx')