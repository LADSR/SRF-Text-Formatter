from variables import doc, paragraphs

a = 0
b = str()

def correction(b):
    for paragraph in paragraphs:
        if paragraph.text.startswith(b):
            paragraph.text = '*' + paragraph.text
            paragraph.style = doc.styles['Normal']
        
def correctiontwo(b):
    for paragraph in paragraphs:
        if paragraph.text.startswith(b):
            if paragraph.text.__contains__('?'):
                paragraph.text = ':<small><h2>' + paragraph.text + '</small></h2>'
                paragraph.style = doc.styles['Normal']

            else:
                paragraph.text = '</br><big><i><u>' + paragraph.text + '</big></i></u>'
                paragraph.style = doc.styles['Normal']


def h2(a, b):
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 2'):
            a = a + 1

            if a == 1:
                b = paragraph.text

            if a >= 2:
                paragraph.text = '*' + paragraph.text
                paragraph.style = doc.styles['Normal']
            
        if paragraph.style.name.startswith('Heading 2') == False:
            if paragraph.style.name.startswith('Heading 1') and a == 1:
                correction(b)
                paragraph.style = doc.styles['Normal']
                a = 0
                b = str()

            if a == 1:
                correctiontwo(b)
                a = 0
                b = str()
            
            elif a >= 2:
                correction(b)
                a = 0
                b = str()

            else:
                a = 0
                b = str()  