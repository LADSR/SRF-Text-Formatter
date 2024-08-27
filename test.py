from docx import Document
file = r'C:\Users\Cliff\Desktop\1 OnTrackNorthAmerica Promise Statement.docx'
doc = Document(file)
paragraphs = doc.paragraphs

def colors():
    for paragraph in paragraphs:
        for run in paragraph.runs:
            if run.font.color.rgb:
                color = run.font.color.rgb
                print(color)

colors()