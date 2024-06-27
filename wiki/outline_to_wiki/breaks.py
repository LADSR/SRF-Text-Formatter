from docx import Document
from docx.shared import Pt

from vars import doc, paragraphs
'''and paragraph.style.name.startswith('Heading') == False'''
#Exclude lists
def fix_breaks():
    for paragraph in paragraphs:
        if paragraph.paragraph_format.first_line_indent:
            paragraph.text = ':' + paragraph.text
            #account for para text if text.starts with (<) false
        if paragraph.text.split:
            if paragraph.text.startswith('*') == False and paragraph.text.endswith('</small></h2>') == False and paragraph.text.endswith('</h2></b></i>') == False: 
                paragraph.add_run('</br>')

def blank_space():
    fix_breaks()