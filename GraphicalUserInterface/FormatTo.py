def form_to_wiki():
    global a
    a = True
    if c | b == True:
        c = False
        b = False
    return a
def form_to_outline():
    global b
    b = True
    if a | c == True:
        a = False
        c = False
    return b
def form_to_docx():
    global c
    c = True
    if a | b == True:
        a = False
        b = False
    return c