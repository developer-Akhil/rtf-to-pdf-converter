from spire.doc import Document, FileFormat, XHTMLValidationType
import io

__all__ = ['RtfToPdfM']


class RtfToPdfM:

    def __init__(self, prop):
        self.prop = prop

    @staticmethod
    def rtf_to_pdf_m(new_pdf_fil):
        # from awsglue.utils import read_text,write_pdf
        # rtf_content = read_text("s3://s3-rtf-to-pdf/dataz/src_loc/209457862_2021-06-04.rtf")
        # Convert RTF to PDF using Spire.Doc
        # doc1 = Rtf15Reader.read(BytesIO(new_pdf_fil))
        # print("********************************")
        # print(type(doc1))
        # outval = PlaintextWriter.write(doc1).getvalue()
        # outval = ' '.join(outval.split())
        # print(outval)
        doc = Document()
        buffer = io.BytesIO(new_pdf_fil)
        # print(buffer)
        doc.LoadFromStream(stream=buffer, fileFormat=29)
        buffer2 = io.BytesIO()
        doc.SaveToStream(buffer2, FileFormat.PDF)

        # output_buffer_content = buffer.getvalue()

        doc.Close()
        return buffer2.getvalue()

        # # Create a Document instancef
        # doc = Document()
        # # Load a RTF document
        # doc.LoadFromFile(new_pdf_fil, FileFormat.Rtf)
        # # Save it to a PDF
        # doc.SaveToFile(final_pdf, FileFormat.PDF)
        # doc.Close()
