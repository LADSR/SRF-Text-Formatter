#python docx
from docx import Document
from docx.shared import Pt
#tkinter
from tkinter import *
from tkinter import ttk

#custom
#NEEDS DOC FOR DOC SAVE

def main():
    from GraphicalUserInterface.UploadFile import doc
    from GraphicalUserInterface.FormatTo import a
    if a == True:
        from wiki.main import wiki_format
        wiki_format()
        #NOTE: allow people to customize file name
        #Maybe default could be old file name.
        doc.save('Wiki_Out.docx')