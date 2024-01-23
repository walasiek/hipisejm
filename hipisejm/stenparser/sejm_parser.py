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
        self.parsing_state = {}
        self._set_empty_parsing_state()

    def parse_file(self, filepath: str):
        """
        Parses file given from filepath.
        Returns: ???
        """
        self.reader = PdfReader(filepath)
        self.number_of_pages = len(self.reader.pages)

        for page_index in range(self.number_of_pages):
            self._parse_page(page_index)

    def _set_empty_parsing_state(self):
        self.parsing_state['in_speeches'] = True
        self.parsing_state['current_speaker_raw_name'] = None
        self.parsing_state['current_speaker_speech_items'] = []

    def _parse_page(self, page_index):
        logging.debug("Parsing PDF page %i out of %i", page_index + 1, self.number_of_pages)
        current_page = self.reader.pages[page_index]
        raw_text = self._extract_text_from_page(current_page)

        # tutaj usunąć nagłówek i stopkę
        # ominąć pierwsze strony ze spisem treści
        # stworzyć klasę wizytatora który zachowuje formatowanie <i>
        # następnie sparsować

        # todo debug
        print("")
        print(raw_text)
        print("")

    def _extract_text_from_page(self, page):
        visitor_output = []
        def visitor_body(text, cm, tm, font_dict, font_size):
            # ignore header and footer HOW????
            y = tm[5]
            if not (y < 788.0):
                return

            is_bold = False
            is_italic = False

            if font_dict is not None:
                base_font = font_dict.get("/BaseFont", "")
                if "-Italic" in base_font:
                    is_italic = True
                if "-Bold" in base_font:
                    is_bold = True

            added_tags = []
            if is_bold:
                added_tags.append("b")
            if is_italic:
                added_tags.append("i")

            #print("DUPA", added_tags, text)
            added_prefix = "".join([f"<{t}>" for t in added_tags])
            added_suffix = "".join([f"</{t}>" for t in reversed(added_tags)])

            out_text = text
            if not re.match(r"^\s*$", text):
                out_text = f"{added_prefix}{text}{added_suffix}"
            visitor_output.append(out_text)

        page.extract_text(visitor_text=visitor_body)
        text = "".join(visitor_output)
        return text
