from docx import Document
from docx.shared import Pt

def wiki_format():
    from GraphicalUserInterface.FormatFrom import f, e, d
    if f == True:
        #Imports functions
        from wiki.doc_to_wiki.headings import format_headings_and_lists
        from wiki.doc_to_wiki.other import other_text_styles
        from wiki.doc_to_wiki.breaks import blank_space
        
        #Runs functions
        format_headings_and_lists()
        other_text_styles()
        blank_space()
        
        ## FOR Shravanth: Uncomment text below when code is ready
        ##from spellcheck.spell_check import //Main_function_name_here()//
        ##//Main_function_name_here()//

    elif e == True:
        #imports functions
        from wiki.outline_to_wiki.headings import format_headings_and_lists
        from wiki.outline_to_wiki.breaks import fix_breaks
        from wiki.outline_to_wiki.others import other_text_styles

        #runs functions
        format_headings_and_lists()
        other_text_styles()
        fix_breaks()
        
    
    elif d == True:
        print('This document is already in wiki format.')
        print('Please change the original document type.')
    
    else:
        print('ERROR')
       