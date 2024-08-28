import sys
from docx import Document

#dir = '\\Mediawiki\\extensions\\DocumentFormatter'
dir = '/var/www/vhosts/ontrackworld.org/httpdocs/extensions/DocumentFormatter'


page = 'Formatter Testing'
file = dir + '/RE-SEED.docx'
filetype = 1

#Variables imported from special page(php)
'''
if len(sys.argv) > 1:
    try:
    page = sys.argv[1]
    file = sys.argv[2]
    filetype = sys.argv[3]

    except OSError as err:
        print(err)
else:
    print('somethings wrong :(')
'''


#PythonDocx variables
doc = Document(file)
paragraphs = doc.paragraphs