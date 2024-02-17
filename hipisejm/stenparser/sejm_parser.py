import re
import logging
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LAParams, LTTextBox, LTTextLine, LTChar
from pdfminer.pdfparser import PDFParser
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


class SejmParser:
    # need to force line merge due to two column layout to fix text order
    # inspired by: https://github.com/pdfminer/pdfminer.six/issues/276#issuecomment-518010761
    PDF_LINE_MARGIN = 2.0
    PDF_CHAR_MARGIN = 4.0

    """
    Parses transcripts from: https://www.sejm.gov.pl/sejm10.nsf/stenogramy.xsp
    """
    def __init__(self):
        self.number_of_pages = 0
        self.pdf_parser = None

    def parse_file(self, filepath: str):
        """
        Parses file given from filepath.
        Returns: ???
        """
        self.number_of_pages = 0
        raw_results = self._parse_pdf_to_raw(filepath)

    def _parse_pdf_to_raw(self, filepath: str):
        raw_results = []
        with open(filepath, "rb") as pdffile:
            self.pdf_parser = PDFParser(pdffile)
            document = PDFDocument(self.pdf_parser)
            resource_manager = PDFResourceManager()
            laparams = LAParams(
                char_margin=self.PDF_CHAR_MARGIN,
                line_margin=self.PDF_LINE_MARGIN)

            dev = PDFPageAggregator(resource_manager, laparams=laparams)
            intepreter = PDFPageInterpreter(resource_manager, dev)

            for pdf_page in PDFPage.create_pages(document):
                self.number_of_pages += 1

                # debug
                #if self.number_of_pages > 10:
                #    break
                logging.debug("Parsing PDF page %i", self.number_of_pages)

                intepreter.process_page(pdf_page)
                layout = dev.get_result()

                for element in layout:
                    if isinstance(element, LTTextContainer):
                        self._parse_text_container(raw_results, element)

                print("########## END PAGE ##########")


    def _parse_text_container(self, raw_results, text_container):
        for text_line in text_container:

            current_fontname = None
            chunk = []

            for character in text_line:
                if not isinstance(character, LTChar):
                    continue

                if (current_fontname is not None) and (current_fontname != character.fontname):
                    entry = ("".join(chunk), current_fontname, text_line.height)
                    raw_results.append(entry)
                    print(entry)
                    current_fontname = character.fontname
                    chunk = [character.get_text()]
                else:
                    current_fontname = character.fontname
                    chunk.append(character.get_text())
            if len(chunk) > 0:
                entry = ("".join(chunk), current_fontname, text_line.height)
                raw_results.append(entry)
                print(entry)

            print("------ END LINE--------")
        print("==========END BOX==========")

        return raw_results
