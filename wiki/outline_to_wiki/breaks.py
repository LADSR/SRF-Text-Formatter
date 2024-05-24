from docx import Document
from docx.shared import Pt

from vars import doc, paragraphs
'''and paragraph.style.name.startswith('Heading') == False'''
#Exclude lists
def fix_breaks():
    for paragraph in paragraphs:
        if paragraph.paragraph_format.first_line_indent:
            paragraph.text = ':' + paragraph.text

        if paragraph.text.split and paragraph.text.startswith('*') == False and paragraph.style.name.startswith('Heading 2') == False and paragraph.style.name.startswith('Heading 3') == False: 
            paragraph.add_run('</br>')

def blank_space():
    fix_breaks()