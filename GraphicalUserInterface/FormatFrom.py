from GraphicalUserInterface.Vars import d, e, f

def form_from_wiki():
    global d
    from GraphicalUserInterface.Vars import d, e, f
    d = True
    if e | f == True:
        e = False
        f = False
    return d

def form_from_outline():
    global e
    from GraphicalUserInterface.Vars import d, e, f
    e = True
    if d | f == True:
        d = False
        f = False
    return e

def form_from_docx():
    global f
    from GraphicalUserInterface.Vars import d, e, f
    f = True
    if e | d == True:
        e = False
        d = False
    return f

#ACCOUNT FOR MULTI TRUE