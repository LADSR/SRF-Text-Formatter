from variables import color
from word.resources.format_text import format_text
from word.resources.style_text import style_text
from word.resources.breaks import breaks
from word.resources.colors import colors

def format_from_word():
    format_text()
    style_text()
    breaks()
    if color == 1:
        colors()