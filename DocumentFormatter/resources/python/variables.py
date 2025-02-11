import sys, os, pywikibot
from docx import Document

a = 0

#Variables imported from special page(php)
if len(sys.argv) > 1:
    dir = sys.argv[1]
    page = sys.argv[2]
    file = sys.argv[3]
    filetype = int(sys.argv[4])
    
    doc = Document(file)
    paragraphs = doc.paragraphs
    a = a+ 1

else:
    print('broken :(')

if a == 1:
    exec(open('main.py').read())




