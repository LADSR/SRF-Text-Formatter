#Only need doc and format kind
from vars import doc, for_kind

#All scripts should start running from here
#paths need to be changed to dynamic paths that fit diffrent computers
def main():
    try:
        if for_kind == 'ONE':
            from wiki.main import wiki_format
            wiki_format()
            #CHANGE PATH OUT
            doc.save('Wiki_Output.docx')
        
        elif for_kind == 'TWO':
            wiki_format()
            #CHANGE PATH OUT
            doc.save('Outline_Output.docx')
        
        elif for_kind == 'THREE':
            wiki_format()
            #CHANGE PATH OUT
            doc.save('Document_Output.docx')
        
        else:
            print('You did not enter a valid answer. please try again.')
            while for_kind != 'ONE' | 'TWO' | 'THREE':
                main()

    except Exception as e:
        print("An error occurred:", e)


main()
#Doc file            C:\Users\Cliff\Desktop\test.docx
#My Outline          C:\Users\Cliff\Desktop\May 16th 2024 - Copy.docx
#Michael Outline     C:\Users\Cliff\Desktop\RE-SEED.docx