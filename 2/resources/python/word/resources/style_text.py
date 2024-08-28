from variables import doc

def bold_text():
    a = 0
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.bold:
                if a == 0:
                    a = a + 1
                    txt = run.text
                    run.text = ''
                
                elif a >= 1:
                    a = a + 1
                    txt = txt + run.text
                    run.text = ''

            elif run.bold == False:
                    for paragraph in doc.paragraphs:
                        if paragraph.text.__contains__(txt):
                            nurun = '<b>' + txt + '</b>'
                            paragraph.text.replace(txt, nurun)
                            a = 0

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

def style_text():
    bold_text()
    italics_text()
    underline_text()
    strike_text()
    sup_text()
    sub_text()
