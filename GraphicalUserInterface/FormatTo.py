from GraphicalUserInterface.Vars import a, b, c
def form_to_wiki():
    global a, b, c
    a = True
    if c | b == True:
        c = False
        b = False
    return a
def form_to_outline():
    global a, b, c
    b = True
    if a | c == True:
        a = False
        c = False
    return b
def form_to_docx():
    global a, b, c
    c = True
    if a | b == True:
        a = False
        b = False
    return c