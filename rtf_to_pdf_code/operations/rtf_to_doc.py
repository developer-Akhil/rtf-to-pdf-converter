import win32com.client as win32
from win32com.client import constants
from spire.doc import *
import os
import re
import win32api

__all__ = ['RtfToDoc']


class RtfToDoc:

    def __init__(self, prop):
        self.prop = prop

    @staticmethod
    def rtf_to_doc(doc_file: str):
        win32api.FormatMessage(-2147352565)
        word = win32.gencache.EnsureDispatch('Word.Application')
        # in_file = str(os.path.abspath(file_path).replace("c", "C") ) # if the file path in c
        # doc = word.Documents.Open(in_file)

        doc = word.Documents.Open(doc_file)
        doc.Activate()

        # Rename path with .doc
        new_file_abs = os.path.abspath(doc_file)
        new_file_abs = re.sub(r'\.\w+$', '.doc', new_file_abs)

        print(new_file_abs)
        # Save and Close
        word.ActiveDocument.SaveAs(
            new_file_abs, FileFormat=constants.wdFormatDocument
        )
        doc.Close(False)
