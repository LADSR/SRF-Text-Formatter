from GraphicalUserInterface.UploadFile import doc

paragraphs = doc.paragraphs

def savename():
    from Index import fileout
    global name
    name = fileout.get()
    return name