from hipisejm.utils.pdfminer_wrapper import PDFText, PDFLineBreak, PDFTextBoxBreak, PDFPageBreak
from hipisejm.utils.pdfminer_wrapper_helper import get_first_text_box_from_index
import pytest


TEST_DATA1 = [
    PDFText("1 First", "CentSchbookEU-Normal", 10.5),   # index 0
    PDFLineBreak(),
    PDFText("1 Second", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("1 Third", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFText("2 First", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("2 Second", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),  # index 10
    PDFText("2 Third", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFPageBreak(),
    PDFText("3 First", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("3 Second", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    ]


TEST_DATA2 = [
    PDFText("1 First", "CentSchbookEU-Normal", 10.5),   # index 0
    PDFLineBreak(),
    PDFText("1 Second", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("1 Third", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFTextBoxBreak(),
    PDFText("2 First", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(), # index 10
    ]


TEST_DATA3 = [
    PDFTextBoxBreak(), # index 0
    PDFText("1 First", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("1 Second", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("1 Third", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFTextBoxBreak(),
    PDFText("2 First", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    ]


def test_check_extract_from_middle():
    actual = get_first_text_box_from_index(TEST_DATA1, 8)
    assert actual == TEST_DATA1[7:13]


def test_check_extract_from_last_not_closed():
    actual = get_first_text_box_from_index(TEST_DATA1, 14)
    assert actual == TEST_DATA1[14:19]


def test_check_extract_from_first_not_opened():
    actual = get_first_text_box_from_index(TEST_DATA1, 0)
    assert actual == TEST_DATA1[0:6]


def test_check_extract_from_index_on_box():
    actual = get_first_text_box_from_index(TEST_DATA1, 7)
    assert actual == TEST_DATA1[7:13]


def test_check_extract_empty_if_two_boxes():
    actual = get_first_text_box_from_index(TEST_DATA2, 6)
    assert actual == []


def test_check_extract_empty_if_last_is_box():
    actual = get_first_text_box_from_index(TEST_DATA2, 10)
    assert actual == []


def test_check_extract_nonempty_if_first_is_box():
    actual = get_first_text_box_from_index(TEST_DATA3, 0)
    assert actual == TEST_DATA3[1:7]
