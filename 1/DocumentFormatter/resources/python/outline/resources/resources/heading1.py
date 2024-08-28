from variables import doc, paragraphs

def h1():
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 1'):
            #Accounts for beginning quotes
            if paragraph.text.__contains__('“') and paragraph.text.__contains__('”') and paragraph.text.endswith('.') == False:
                paragraph.text = paragraph.text.replace('“', '<big><b><i> “')
                paragraph.text = paragraph.text.replace('”', '”</i></big></b>')
                paragraph.text = '<center><big><b>' + paragraph.text + '</center></big></b>'
                paragraph.style = doc.styles['Normal']

            elif paragraph.text.__contains__('?'):
                paragraph.text = '<h2><b><i>' + paragraph.text + '</h2></b></i>'

            elif paragraph.text.endswith('.') == False and paragraph.text.startswith('<') == False:
                paragraph.text = '<center><big><big>' + paragraph.text + '</center></big></big>'
                paragraph.style = doc.styles['Normal']

            else:
                paragraph.style = doc.styles['Normal']