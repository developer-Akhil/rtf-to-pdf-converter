from spire.doc import *
# import win32com.client as win32
# from win32com.client import constants

__all__ = ['DocToPdf']


class DocToPdf:

    def __init__(self, prop):
        self.prop = prop

    def doc_to_pdf(self, doc_file: str, pdf_file: str):
        document = Document()
        document.LoadFromFile(doc_file)

        # document.LoadFromFile("Sample.doc")
        # Save the file to a PDF file
        document.SaveToFile(pdf_file, FileFormat.PDF)
        document.Close()

