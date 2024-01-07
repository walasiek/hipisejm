import os
from hipisejm.stenparser.sejm_parser import SejmParser


SAMPLE_PDF_FILEPATH = os.path.join("resources", "test_data", "01_j_ksiazka.pdf")


def test_simple():
    parser = SejmParser()
    assert parser is not None, "SejmParser created and not None"
    assert os.path.isfile(SAMPLE_PDF_FILEPATH), f"File: {SAMPLE_PDF_FILEPATH} exists"
