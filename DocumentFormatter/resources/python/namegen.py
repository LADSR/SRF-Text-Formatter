import random  
import string
import docxpy

#create name
tempname = ''.join((random.choice(string.ascii_letters) for x in range(8))) + '.docx'
path = '/var/www/vhosts//hungry-franklin.74-208-238-145.plesk.page/httpdocs/extensions/DocumentFormatter/tmp/' + tempname

def gettext():
    global doctext
    doctext = docxpy.process(path)
    return doctext
