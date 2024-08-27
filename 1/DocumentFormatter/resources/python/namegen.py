import random  
import string
from variables import dir

from spire.doc.common import *
from spire.doc import *

#create name
tempname = ''.join((random.choice(string.ascii_letters) for x in range(8))) + '.docx'

path = dir + '/tmp/' + tempname

def gettext():
    global doctext
    document = Document()
    document.LoadFromFile(path)
    doctext = document.GetText()
    return doctext
