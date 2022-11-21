from docx import Document

document = Document("resume.docx")
paragraph = document.paragraphs[0]
print(paragraph.text)