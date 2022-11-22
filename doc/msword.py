from docx import Document

document = Document("Ashok.docx")
paragraph = document.paragraphs[0]
print(paragraph.text)