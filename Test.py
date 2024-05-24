'''
This  is where i test and debug functions that aren't working
A good method is to print the paragraph or run's name and go from there

'''
#NO TOUCH vvvvvv
from docx import Document
from docx.shared import Pt

doc_path = r'C:\Users\Cliff\Desktop\RE-SEED.docx'
doc = Document(doc_path)
paragraphs = doc.paragraphs
sections = doc.sections
#NO TOUCH ^^^^^

''' Examples

#Checks runs
def bold_text():
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.bold:
                run.text = '<b>' + run.text + '</b>'
                run.bold = False

#Checks para
for paragraph in paragraphs:
        if paragraph.style.name.startswith('Title'):
            paragraph.text = '<center><h1>' + paragraph.text + '</h1></center>'
            paragraph.style = doc.styles['Normal']if paragraph.style.name.startswith('Heading 2'):
            i = i + 1
        else:
            continue

        for paragraph in doc.paragraphs:
            if paragraph.style.name.startswith('Heading 2') and i >= 3:
                paragraph.text = '* <h3>' + paragraph.text + '</h3>'
                paragraph.style = doc.styles['Normal']
                if paragraph.style.name.startswith('Heading 2') == False:
                    i = 0

            elif paragraph.style.name.startswith('Heading 2') and i < 3:
                paragraph.text = '<h3>' + paragraph.text + '</h3>'
                paragraph.style = doc.styles['Normal']
                if paragraph.style.name.startswith('Heading 2') == False:
                    i = 0
    print(paragraph.text)
    
    print(aa)
'''
aa = 0
for p in doc.paragraphs:
    if p.style.name.startswith('Heading 2'):
        p.text = '*' + p.text
        aa = aa = 1
        print(p.style.name)
        print(p.text)
        
    elif p.style.name.startswith('Heading 2') == False and aa < 3:
        aa = 0
        print(p.style.name)
        print(p.text)



        
#NO TOUCH
#Doc file            C:\Users\Cliff\Desktop\test.docx
#My Outline          C:\Users\Cliff\Desktop\May 16th 2024 - Copy.docx
#Michael Outline    C:\Users\Cliff\Desktop\RE-SEED.docx