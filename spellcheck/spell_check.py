# install required packages
from docx import Document
## Push spell Module to git or correct path
from autocorrect import Speller

# load word document
## import doc from vars.py file in root directory
doc = Document("Trial.docx")

# initialize speller for autocorrection
spell = Speller()

# autocorrect text function
def autocorrect_text(text):
    ## text.split doesn't give you seprate words it detects spaces inbetween the words.
    ## the words variable is predefined so you'll have to save output to 'word' or a diffrent variable name
    ## the words funcion gets letters instead of words

    # Tokenize the text into words
    words = text.split()
    corrected_words = []
    
    # autocorrect each word
    for word in words:
        corrected_word = spell(word)
        corrected_words.append(corrected_word)
    
    # join corrected words keeping spaces intact
    return ' '.join(corrected_words)

# iterate through each paragraph in the document
for para in doc.paragraphs:
    # autocorrect the text
    autocorrected_text = autocorrect_text(para.text)
    
    # update paragraphs with autocorrected text
    para.text = autocorrected_text

# save the autocorrected document
## don't save document here just run function from main from the wiki directory
## See run.py comments for example
doc.save("Cleaned_Document.docx")
print("Autocorrected document saved as Cleaned_Document.docx")
