import sys
from docx import Document

dir = sys.argv[1]
page = sys.argv[2]
file = sys.argv[3]
filetype = int(sys.argv[4])
color = int(sys.argv[5])

doc = Document(file)
paragraphs = doc.paragraphs
#exec(open('main.py').read())