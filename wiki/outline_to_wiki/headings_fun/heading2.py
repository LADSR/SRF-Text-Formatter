from docx import Document
from docx.shared import Pt
from vars import doc, paragraphs

a = 0
b = str()
def correction(b):
    for paragraph in paragraphs:
        if paragraph.text.startswith(b):
            paragraph.text = '*' + paragraph.text
            paragraph.style = doc.styles['Normal']

def h2(a, b):
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 2'):
            if paragraph.text.__contains__('?') and paragraph.text.startswith('<') == False and paragraph.text.startswith(':') == False:
                a = a + 1
                if a == 1:
                    b = paragraph.text

                if a >= 2:
                    paragraph.text = ':*' + paragraph.text
                
            if paragraph.style.name.startswith('Heading 2') == False:
                if a >= 2:
                    correction(b)
                    a = 0
                    b = str()
                else:
                    a = 0
                    b = str()
            else:
                paragraph.text = '*' + paragraph.text
                paragraph.style = doc.styles['Normal']