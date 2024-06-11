def main():
    from GraphicalUserInterface.FormatTo import a
    from GraphicalUserInterface.UploadFile import doc
    from Index import path
    
    if a == True:
        from wiki.main import wiki_format
        wiki_format()
        doc.save(path)