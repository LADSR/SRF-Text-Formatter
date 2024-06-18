import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def main():
    from GraphicalUserInterface.FormatTo import a
    from GraphicalUserInterface.UploadFile import doc
    
    if a == True:
        from wiki.main import wiki_format
        wiki_format()
        doc.save(desktop + '\\' + 'wiki.docx')