import codecs
import json
import re
import boto3

__all__ = ['Configuration']


class Configuration(object):

    def __init__(self, bucket_nm, prop_file_nm):
        self.dist_prefix = None
        self.src_prefix = None
        self.dist_bucket = None
        self.new_pdf_file = None
        self.doc_file = None
        self.pdf_file = None
        self.src_bucket = None
        self.pdf_str = None
        self.final_pdf = None
        self.bucket_nm = bucket_nm
        self.prop_file_nm = prop_file_nm

    def get_file(self):
        s3 = boto3.resource('s3')
        obj = s3.Object(self.bucket_nm, self.prop_file_nm)
        line_stream = codecs.getreader("utf-8")
        return json.load(line_stream(obj.get()['Body']))

    def config(self):
        self.pdf_str = "Evaluation Warning: The document was created with Spire.Doc for Python."
        self.src_bucket = self.get_file()['rtf_to_pdf']['src_bucket']
        self.dist_bucket = self.get_file()['rtf_to_pdf']['dist_bucket']
        self.src_prefix = self.get_file()['rtf_to_pdf']['src_prefix']
        self.dist_prefix = self.get_file()['rtf_to_pdf']['dist_prefix']
        # self.doc_file = self.get_file()['rft_to_pdf']['doc_file']
        # self.pdf_file = self.get_file()['rft_to_pdf']['pdf_file']
        # self.new_pdf_file = self.get_file()['rft_to_pdf']['new_pdf_file']
        # self.final_pdf = self.get_file()['rft_to_pdf']['final_pdf']