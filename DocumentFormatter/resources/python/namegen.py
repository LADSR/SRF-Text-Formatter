import random  
import string
import docxpy
from variables import dir
#create name
tempname = ''.join((random.choice(string.ascii_letters) for x in range(8))) + '.docx'
path =  dir +'/tmp/' + tempname

def gettext():
    global doctext
    doctext = docxpy.process(path)
    return doctext