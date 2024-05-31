# install required packages
from docx import Document
from autocorrect import Speller

# load word document
doc = Document("Trial.docx")

# initialize speller for autocorrection
spell = Speller()

# autocorrect text function
def autocorrect_text(text):
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
doc.save("Cleaned_Document.docx")
print("Autocorrected document saved as Cleaned_Document.docx")
