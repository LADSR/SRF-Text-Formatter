import sys, os, pywikibot
from docx import Document

#python3 ./variables.py Formatter_Testing /var/www/vhosts/wiki.ontracknorthamerica.org/httpdocs/images/a/ab/4_NM_Sustainable_Forestry_Business_Plan_Outline_23Feb2023.docx 1
#dir = '\\Mediawiki\\extensions\\DocumentFormatter'
dir = '/var/www/vhosts/wiki.ontracknorthamerica.org/httpdocs/extensions/DocumentFormatter'
a = 0


#Variables imported from special page(php)

page = sys.argv[1]
file = sys.argv[2]
filetype = int(sys.argv[3])

doc = Document(file)
paragraphs = doc.paragraphs
exec(open('main.py').read())