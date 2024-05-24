from docx import Document
from docx.shared import Pt

#IT WORKS!!!
print('What format was your document origanally in?')
form_type = input('type ONE for Word Document or TWO for outline. ')

def wiki_format():
    if form_type == 'ONE':
        #Imports functions
        from wiki.doc_to_wiki.headings import format_headings_and_lists
        from wiki.doc_to_wiki.other import other_text_styles
        from wiki.doc_to_wiki.breaks import blank_space
        
        #Runs functions
        other_text_styles()
        format_headings_and_lists()
        blank_space()

    elif form_type == 'TWO':
        #imports functions
        from wiki.outline_to_wiki.headings import format_headings_and_lists
        from wiki.outline_to_wiki.breaks import fix_breaks
        from wiki.outline_to_wiki.others import other_text_styles

        #runs functions
        other_text_styles()
        fix_breaks()
        format_headings_and_lists()
       