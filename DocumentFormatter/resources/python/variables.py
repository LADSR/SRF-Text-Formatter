import sys
from docx import Document

dir = '/var/www/vhosts/hungry-franklin.74-208-238-145.plesk.page/httpdocs/extensions/DocumentFormatter'
a = 0

page = sys.argv[1]
file = sys.argv[2]
filetype = int(sys.argv[3])

doc = Document(file)
paragraphs = doc.paragraphs
exec(open('main.py').read())