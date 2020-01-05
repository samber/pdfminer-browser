#import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator


# Open a PDF document.
#fp = open(sys.argv[1], 'rb')
fp = open("example.pdf", 'rb')

parser = PDFParser(fp)
document = PDFDocument(parser, "")
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()

# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)


def get_table_content():
    # Get the outlines of the document.
    outlines = document.get_outlines()
    for (level, title, dest, a, se) in outlines:
        print(level, title, dest, a, se)


def process_pages():
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        # receive the LTPage object for the page.
        layout = device.get_result()
        print(layout)
        for element in layout:
            print(element)
        print("\n\n\n")


get_table_content()
process_pages()
