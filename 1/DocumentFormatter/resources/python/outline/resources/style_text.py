from variables import doc, paragraphs

def bold_text():
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.bold:
                run.text = '<b>' + run.text + '</b>'
                run.bold = False

def italics_text():
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.italic:
                run.text = '<i>' + run.text + '</i>'
                run.italic = False

def underline_text():
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.underline:
                run.text = '<u>' + run.text + '</u>'
                run.underline = False

def strike_text():
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.font.strike:
                run.text = '<s>' + run.text + '</s>'
                run.font.strike = False

def sub_text():
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.font.subscript:
                run.text = '<SUB>' + run.text + '</SUB>'
                run.font.subscript = False

def sup_text():
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.font.superscript:
                run.text = '<SUP>' + run.text + '</SUP>'
                run.font.superscript = False

def quotes():
    #quote over rides heading styles
    for paragraph in paragraphs:
        if paragraph.text.__contains__('“') and paragraph.text.__contains__('”') and paragraph.text.startswith('<') == False:
            #Makes actual quote itallic
            paragraph.text = paragraph.text.replace('“', '<i> “')
            paragraph.text = paragraph.text.replace('”', '”</i>')
            paragraph.style = doc.styles['Normal']

def questions():
    for paragraph in doc.paragraphs:
        if paragraph.text.__contains__('?') and paragraph.style.name.startswith('Heading 2') == False and paragraph.text.startswith(':') == False and paragraph.text.startswith('*') == False:
            if paragraph.text.startswith('Who'):
                paragraph.text = '<h2><i><b>' + paragraph.text + '</b></i></h2>'
            if paragraph.text.startswith('What'):
                paragraph.text = '<h2><i><b>' + paragraph.text + '</b></i></h2>'
            if paragraph.text.startswith('When'):
                paragraph.text = '<h2><i><b>' + paragraph.text + '</b></i></h2>'
            if paragraph.text.startswith('Where'):
                paragraph.text = '<h2><i><b>' + paragraph.text + '</b></i></h2>'
            if paragraph.text.startswith('Why'):
                paragraph.text = '<h2><i><b>' + paragraph.text + '</b></i></h2>'
            if paragraph.text.startswith('How'):
                paragraph.text = '<h2><i><b>' + paragraph.text + '</b></i></h2>'
            if paragraph.text.startswith('Are'):
                paragraph.text = '<h2><i><b>' + paragraph.text + '</b></i></h2>'
            if paragraph.text.startswith('Should'):
                paragraph.text = '<h2><i><b>' + paragraph.text + '</b></i></h2>'
            else:
                continue

def style_text():
    bold_text()
    italics_text()
    underline_text()
    strike_text()
    sup_text()
    sub_text()
    quotes()