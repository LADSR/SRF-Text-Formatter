from docx import Document
from docx.shared import Pt

from vars import doc, paragraphs

def fix_breaks():
    for paragraph in paragraphs:
        if paragraph.paragraph_format.first_line_indent:
            paragraph.text = ':' + paragraph.text

        if paragraph.text.split:
            paragraph.add_run('</br>')

def blank_space():
    fix_breaks()
    