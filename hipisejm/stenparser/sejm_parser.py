import re
import logging
from pdfminer.layout import LAParams
from hipisejm.utils.pdfminer_wrapper import PDFMinerWrapper


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
        if raw_results is not None:
            # tu zaczyna się zabawa
            pass

        return raw_results

    def _parse_pdf_to_raw(self, filepath: str):
        raw_results = []
        with open(filepath, "rb") as pdffile:
            laparams = LAParams(
                char_margin=self.PDF_CHAR_MARGIN,
                line_margin=self.PDF_LINE_MARGIN)
            pdfminer_wrapper = PDFMinerWrapper(
                pdffile,
                laparams=laparams,
                print_parse=False)  # for DEBUG, in real life set to False!
            pdfminer_wrapper.parse()
            self.number_of_pages = pdfminer_wrapper.number_of_pages

            return pdfminer_wrapper.parsed_data
        return None
