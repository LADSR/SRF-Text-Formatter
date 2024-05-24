from docx import Document
from docx.shared import Pt



doc_path = input("Path to your Document: ")
doc = Document(doc_path)

print('How do you want to format your document?')
for_kind = input('Type ONE for wiki, TWO for outline, and THREE for doc. ')

paragraphs = doc.paragraphs