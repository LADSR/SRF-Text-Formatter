from variables import paragraphs

def colors():
    for paragraph in paragraphs:
        for run in paragraph.runs:
            if run.font.color.rgb and run.text.endswith('</span>') == False:
                color = run.font.color.rgb
                run.text = '<span style=color:#' + str(color) + ';>' + run.text + '</span>'