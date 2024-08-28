#Location: /usr/local/lib/python3.10/dist-packages/pywikibot/families
from pywikibot import family

class Family(family.Family):
    name = 'ontrackwiki'
    langs = {
        'en': 'ontrackworld.org/api.php'
    }