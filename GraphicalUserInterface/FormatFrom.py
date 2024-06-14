from GraphicalUserInterface.Vars import d, e, f

def form_from_wiki():
    global d
    from GraphicalUserInterface.Vars import d
    d = True
    return d

def form_from_outline():
    global e
    from GraphicalUserInterface.Vars import e
    e = True
    return e

def form_from_docx():
    global f
    from GraphicalUserInterface.Vars import f
    f = True
    return f

#ACCOUNT FOR MULTI TRUE