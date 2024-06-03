from docx import Document
from docx.shared import Pt

doc_path = r'PATH HERE'
doc = Document(doc_path)
paragraphs = doc.paragraphs

#Checks para
for paragraph in paragraphs:
    if paragraph.style.name.startswith('Heading 1') and paragraph.text.__contains__('“') == False:
        paragraph.text = '<big><big>' + paragraph.text + '</big></big>'
        paragraph.style = doc.styles['Normal']
    print(paragraph.text)