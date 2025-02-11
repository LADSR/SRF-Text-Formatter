from variables import doc, paragraphs
from outline.resources.resources.heading1 import h1
from outline.resources.resources.heading2 import h2, a, b
from outline.resources.resources.heading3 import h3, c, d

def heading_text():
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 4'):
            paragraph.text = '::*' + paragraph.text
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('Heading 5'):
            paragraph.text = ':::*' + paragraph.text
            paragraph.style = doc.styles['Normal']

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

def format_text():
    h1()
    h3(c,d)
    heading_text()
    title_text()
    h2(a,b)