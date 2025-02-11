from variables import paragraphs

def indents():
    for paragraph in paragraphs:
        if paragraph.paragraph_format.first_line_indent:
            paragraph.text = ':' + paragraph.text

def linebreaks():
    for paragraph in paragraphs:
        if paragraph.text.split:
            if paragraph.text.startswith('*') == False and paragraph.text.endswith('</small></h2>') == False and paragraph.text.endswith('</h2></b></i>') == False: 
                paragraph.add_run('</br>')

def breaks():
    indents()
    linebreaks()