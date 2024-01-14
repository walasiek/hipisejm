import re
import logging
from pypdf import PdfReader


class SejmParser:
    """
    Parses transcripts from: https://www.sejm.gov.pl/sejm10.nsf/stenogramy.xsp
    """
    def __init__(self):
        self.reader = None
        self.number_of_pages = 0

    def parse_file(self, filepath: str):
        """
        Parses file given from filepath.
        Returns: ???
        """
        self.reader = PdfReader(filepath)
        self.number_of_pages = len(self.reader.pages)

        for page_index in range(self.number_of_pages):
            self._parse_page(page_index)

    def _parse_page(self, page_index):
        logging.debug("Parsing PDF page %i out of %i", page_index + 1, self.number_of_pages)

        current_page = self.reader.pages[page_index]
        text = current_page.extract_text()

        # tutaj usunąć nagłówek i stopkę
        # ominąć pierwsze strony ze spisem treści
        # stworzyć klasę wizytatora który zachowuje formatowanie <i>
        # następnie sparsować

        # todo debug
        print("")
        print(text)
        print("")
