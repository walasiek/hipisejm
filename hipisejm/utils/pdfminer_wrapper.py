"""
Wraps some PDFMiner functions to simplify text extraction
"""
import re
import logging
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LAParams, LTTextBox, LTTextLine, LTChar
from pdfminer.pdfparser import PDFParser
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from typing import BinaryIO


def clean_fontname(fontname: str) -> str:
    """
    Returns fontname without hashed prefix, e.g.:
    UYJZJF+CentSchbookEU-Normal -> CentSchbookEU-Normal
    """
    fontname = re.sub(r"^[A-Z]+[+]", "", fontname)
    return fontname


class PDFMinerWrapper:
    def __init__(self, file_to_parse: BinaryIO, laparams: LAParams = None):
        """
        params:
        filepath - file to be parsed
        laparams - if None, then uses PDFMiner default LAParams, otherwise uses LAParams provided here
        """
        self.parsed_data = []
        self.number_of_pages = 0

        self.pdf_parser = PDFParser(file_to_parse)
        self.resource_manager = PDFResourceManager()

        self.dev = PDFPageAggregator(self.resource_manager, laparams=laparams)
        self.intepreter = PDFPageInterpreter(self.resource_manager, self.dev)

    def parse(self):
        self.parsed_data = []
        self.number_of_pages = 0

        document = PDFDocument(self.pdf_parser)
        for pdf_page in PDFPage.create_pages(document):
            self.number_of_pages += 1

            # debug
            #if self.number_of_pages > 10:
            #    break
            logging.debug("Parsing PDF page %i", self.number_of_pages)

            self.intepreter.process_page(pdf_page)
            layout = self.dev.get_result()

            for element in layout:
                if isinstance(element, LTTextContainer):
                    self._parse_text_container(element)

            print("########## END PAGE ##########")

    def _parse_text_container(self, text_container):
        # TODO
        # 1. zrobić test na odrzucanie containerów, linii
        # np. odrzucić nagłówki
        # 2. dodać różne logiczne znaczniki np. koniec linii, koniec kontenera, koniec strony
        for text_line in text_container:

            current_fontname = None
            chunk = []

            for character in text_line:
                if not isinstance(character, LTChar):
                    continue

                if (current_fontname is not None) and (current_fontname != character.fontname):
                    entry = ("".join(chunk), current_fontname, text_line.height)
                    self.parsed_data.append(entry)
                    print(entry)
                    print("FONTFONT" + "\t" + entry[1])
                    current_fontname = character.fontname
                    chunk = [character.get_text()]
                else:
                    current_fontname = character.fontname
                    chunk.append(character.get_text())
            if len(chunk) > 0:
                entry = ("".join(chunk), current_fontname, text_line.height)
                self.parsed_data.append(entry)
                print(entry)

            print("------ END LINE--------")
        print("==========END BOX==========")
