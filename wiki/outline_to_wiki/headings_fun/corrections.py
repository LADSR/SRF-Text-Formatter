from docx import Document
from docx.shared import Pt
from vars import doc, paragraphs
a = 0
b = str()
c = str()
#Correction one runs if two former paragraphs need to formated into bullet points
def h2_correction_one():
    for paragraph in doc.paragraphs:
            if paragraph.text.startswith('tOdjewZ7wd '):
                if paragraph.text.startswith(b) or paragraph.text.startswith(c):
                    paragraph.text = paragraph.text.replace('tOdjewZ7wd ', '')
                    paragraph.text = paragraph.text.replace(' tUDK9aIVL1', '')

#Correction Two Removes Custom strings from non bullet text
def h2_correction_two():
    from vars import doc, paragraphs
    for paragraph in doc.paragraphs:
        if paragraph.text.startswith('tOdjewZ7wd '):
            if paragraph.text.startswith(b) or paragraph.text.startswith(c):
                paragraph.text = paragraph.text.replace('tOdjewZ7wd ', '*<h3>')
                paragraph.text = paragraph.text.replace(' tUDK9aIVL1', '</h3>')
