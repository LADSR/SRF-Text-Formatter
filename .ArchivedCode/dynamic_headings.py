from docx import Document
from docx.shared import Pt

from vars import doc, paragraphs
a = 0
b = str('')
c = str('')

def heading_2(a, b, c):
    for paragraph in doc.paragraphs:
        if paragraph.style.name.startswith('Heading 2') and paragraph.text.startswith('<') == False and paragraph.text.startswith('*') == False and paragraph.text.startswith('tOdjewZ7wd') == False:
                a = a + 1
                paragraph.text = 'tOdjewZ7wd ' + paragraph.text + ' tUDK9aIVL1'
                #Stores text to refrence later during correction
                if a < 3:
                    if a == 1:
                        b = paragraph.text

                    elif a == 2:
                        c = paragraph.text
                
                #Changes third or more paragraphs into bullets
                elif a >= 3 and paragraph.style.name.startswith('Heading 2') and paragraph.text.startswith('tOdjewZ7wd'):
                    paragraph.text = paragraph.text.replace('tOdjewZ7wd ', '*')
                    paragraph.text = paragraph.text.replace(' tUDK9aIVL1', '')

        #Makes corrections and resets variables whenever heading is no longer heading 2
        elif paragraph.style.name.startswith('Heading 2') == False:
            if a < 3:
                from wiki.outline_to_wiki.headings_fun.corrections import h2_correction_one
                h2_correction_one()
                a = 0
                b = str('')
                c = str('')

            elif a >= 3:
                from wiki.outline_to_wiki.headings_fun.corrections import h2_correction_two
                h2_correction_two()
                a = 0
                b = str('')
                c = str('')
