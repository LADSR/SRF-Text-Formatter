from variables import doc, paragraphs

def heading_text():
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 1'):
            paragraph.text = '<h1>' + paragraph.text + '</h1>'
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('Heading 2'):
            paragraph.text = '<h2>' + paragraph.text + '</h2>'
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('Heading 3'):
            paragraph.text = '<h3>' + paragraph.text + '</h3>'
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('Heading 4'):
            paragraph.text = '<h4>' + paragraph.text + '</h4>'
            paragraph.style = doc.styles['Normal']

        if paragraph.style.name.startswith('Heading 5'):
            paragraph.text = '<h5>' + paragraph.text + '</h5>'
            paragraph.style = doc.styles['Normal']
        
        if paragraph.style.name.startswith('Heading 6'):
            paragraph.text = '<h6>' + paragraph.text + '</h6>'
            paragraph.style = doc.styles['Normal']

        #Wiki doesn't have h7-h9 so it just formats to normal text
        if paragraph.style.name.startswith('Heading 7'):
            paragraph.text = paragraph.text
            paragraph.style = doc.styles['Normal']
        
        if paragraph.style.name.startswith('Heading 8'):
            paragraph.text = paragraph.text
            paragraph.style = doc.styles['Normal']
        
        if paragraph.style.name.startswith('Heading 9'):
            paragraph.text = paragraph.text
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

def format_text():
    heading_text()
    title_text()