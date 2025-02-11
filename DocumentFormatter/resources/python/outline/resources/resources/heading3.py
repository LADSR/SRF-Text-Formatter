from variables import doc, paragraphs

c = 0
d = str()

def correction(d):
    for paragraph in paragraphs:
        if paragraph.text.startswith(d):
            paragraph.text = ':<u>' + paragraph.text + '</u>'
            paragraph.style = doc.styles['Normal']

def correctiontwo(d):
    for paragraph in paragraphs:
        if paragraph.text.startswith(d) and paragraph.text.startswith(':') == False and paragraph.style.name.startswith('Heading 3'):
            paragraph.text = ':*' + paragraph.text
            paragraph.style = doc.styles['Normal']

def h3(c,d):
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 3'):
            c = c + 1
            
            if c == 1:
                d = paragraph.text
            
            if c >= 2:
                paragraph.text = ':*' + paragraph.text

        if paragraph.style.name.startswith('Heading 3') == False:
            if c == 1:
                correction(d)
                c = 0
                d = str()

            else:
                correctiontwo(d)
                c = 0
                d = str()