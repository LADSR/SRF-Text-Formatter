from tkinter import *
from tkinter import ttk
import os 
from tkinter import filedialog

from docx import Document
from docx.shared import Pt

def UploadAction():
    global doc, doc_path, path
    filein = filedialog.askopenfilename()
    path = os.path.abspath(filein)
    doc_path = path
    doc = Document(doc_path)
    print(doc)
    return doc_path, doc, path