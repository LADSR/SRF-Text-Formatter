#!/usr/bin/env python3

import os
import pywikibot

site = pywikibot.Site("en", "ontrackwiki")


def main():
    #runs variables file
    exec(open("variables.py").read())

    #imports
    from variables import filetype, page, doc, dir, file
    from namegen import tempname, gettext

    #defines which page to  edit for pywikibot
    page = pywikibot.Page(site, page)
    try:
        if filetype == 0:
            #Formats document
            from word.main import format_from_word
            format_from_word()
            #save doc to randomized name in tmp dir
            doc.save(dir + '/tmp/' + tempname)
            #extracts text from tmp doc
            gettext()
            from namegen import doctext
            
            #replaces page text with extracted text and saves page
            txt = page.text
            page.text = page.text.replace(txt, doctext)
            page.save('Automatic uplod by document formatter')
            #deletes tmp doc
            os.remove(dir + '/tmp/' + tempname)

            #outputs on success
            print('Success!')

        elif filetype == 1:
            #Formats document
            from outline.main import format_from_outline
            format_from_outline()

            #save doc to randomized name in tmp dir
            doc.save(dir + '/tmp/' + tempname)

            #extracts text from tmp doc
            gettext()
            from namegen import doctext

            #replaces page text with extracted text and saves page
            txt = page.text
            page.text = page.text.replace(txt, doctext)
            page.save('Automatic uplod by document formatter')

            #deletes tmp doc
            os.remove(dir + '/tmp/' + tempname)

            #outputs on success
            print('Success!')
            

    except OSError as err:
        print('Uh Oh! There was a problem')
        print(err)

main()