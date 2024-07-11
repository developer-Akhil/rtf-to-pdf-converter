from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import ContentStream, NameObject, TextStringObject

__all__ = ['MarkerRemover']


class MarkerRemover:
    def __init__(self, prop):
        self.prop = prop
        self.replace_with = ""

    def marker_remover(self, pdf_file: str, new_pdf_file: str):
        reader = PdfReader(pdf_file)
        writer = PdfWriter()

        for page in reader.pages:
            # Get the current page's contents
            content_object = page["/Contents"]
            content = ContentStream(content_object, reader)

            # Loop over all pdf elements
            for operands, operator in content.operations:

                # Was told to adapt this part dependent on my PDF file
                if operator == b"TJ":
                    text = operands[0][0]
                    if isinstance(text, TextStringObject) and text.startswith(
                            self.prop.pdf_str
                    ):
                        operands[0] = TextStringObject(self.replace_with)

            # Set the modified content as content object on the page
            page.__setitem__(NameObject("/Contents"), content)

            writer.add_page(page)

        with open(new_pdf_file, "wb") as fh:
            writer.write(fh)
