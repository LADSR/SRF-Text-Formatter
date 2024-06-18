from docx import Document
from docx.shared import Pt

from vars import doc, paragraphs
from wiki.outline_to_wiki.headings_fun.heading1 import h1
from wiki.outline_to_wiki.headings_fun.heading2 import h2, a, b
def heading_text():
    h1()
    h2(a,b)
    for paragraph in paragraphs:
        '''
        if paragraph.style.name.startswith('Heading 2'):
            if paragraph.text.__contains__('?'):
                paragraph.text = '<h2>' + paragraph.text + '</h2>'
                paragraph.style = doc.styles['Normal']
            else:
                paragraph.text = '*' + paragraph.text
        '''
        if paragraph.style.name.startswith('Heading 3'):
            paragraph.text = ':*'  + paragraph.text
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('Heading 4'):
            paragraph.text = '::*' + paragraph.text
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('Heading 5'):
            paragraph.text = ':::*' + paragraph.text
            paragraph.style = doc.styles['Normal']
#could make it indent
        if paragraph.style.name.startswith('Heading 6'):
            paragraph.text = '::::*' + paragraph.text
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('Heading 7'):
            paragraph.text = ':::::*' + paragraph.text
            paragraph.style = doc.styles['Normal']
        
        if paragraph.style.name.startswith('Heading 8'):
            paragraph.text = '::::::*' + paragraph.text
            paragraph.style = doc.styles['Normal']
        
        if paragraph.style.name.startswith('Heading 9'):
            paragraph.text = ':::::::*' + paragraph.text
            paragraph.style = doc.styles['Normal']

def title_text():
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Title'):
            paragraph.text = '<center><h1>' + paragraph.text + '</h1></center>'
            paragraph.style = doc.styles['Normal']
        
        if paragraph.style.name.startswith('Subtitle'):
            paragraph.text = '<center>' + paragraph.text + '</center>'
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('TOC'):
           paragraph.add_run('__TOC__')
           paragraph.style = doc.styles['Normal']
           print('Please delte the Table of Contents before copy and pasting into the wiki!')

def format_headings_and_lists():
    heading_text()
    title_text()