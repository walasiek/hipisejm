from hipisejm.utils.pdfminer_wrapper import PDFText, PDFLineBreak, PDFTextBoxBreak, PDFPageBreak
from hipisejm.utils.pdfminer_wrapper_helper import get_first_text_box_from_index, get_first_page_from_index, extract_text_from_parsed_list
import pytest


TEST_DATA_TEXT_BOXES1 = [
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


TEST_DATA_TEXT_BOXES2 = [
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


TEST_DATA_TEXT_BOXES3 = [
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


TEST_DATA_PAGES1 = [
    PDFTextBoxBreak(), # index 0
    PDFText("1 First", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("1 Second", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("1 Third", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFPageBreak(),
    PDFTextBoxBreak(),
    PDFText("2 First", "CentSchbookEU-Normal", 10.5), # index 10
    PDFLineBreak(),
    PDFTextBoxBreak(),
    ]


TEST_DATA_EXTRACT_TEXT1 = [
    PDFText("Pani Katarzyna Pełczyńska-Nałęcz ", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("będzie ministrą funduszy i polityki regionalnej", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFText("Pan Jan Kowalski", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFPageBreak(),
    ]


TEST_DATA_EXTRACT_TEXT2 = [
    PDFText("Pani Katarzyna Pełczyńska-Nałęcz (", "CentSchbookEU-Normal", 10.5),
    PDFText("Oklaski", "CentSchbookEU-Italic", 10.6995),
    PDFText(") bę-", "CentSchbookEU-Normal", 10.6995),
    PDFLineBreak(),
    PDFText("dzie ministrą funduszy i polityki regionalnej. Nie ", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("mogę na nią spojrzeć, bo nie jest posłanką. Jest pani ", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("minister? A, jest. (", "CentSchbookEU-Normal", 10.6995),
    PDFText("Oklaski", "CentSchbookEU-Italic", 10.6995),
    PDFText(") Jestem naprawdę bardzo ", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("usatysfakcjonowany, że będziemy razem pracowali ", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    ]


TEST_DATA_EXTRACT_TEXT3 = [
    PDFText("Pani Katarzyna Pełczyńska-Nałęcz ", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFText("będzie ministrą funduszy i polityki regionalnej", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFText("Pan Jan Kowalski (", "CentSchbookEU-Normal", 10.5),
    PDFText("Oklaski", "CentSchbookEU-Italic", 10.5),
    PDFText(") ", "CentSchbookEU-Normal", 10.5),
    PDFText("koniec", "CentSchbookEU-Bold", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFPageBreak(),
    ]


TEST_DATA_EXTRACT_TEXT4 = [
    PDFText("Pan Jan Kowalski (", "CentSchbookEU-Normal", 10.5),
    PDFText("Dzwo-", "CentSchbookEU-Italic", 10.5),
    PDFLineBreak(),
    PDFText("nek", "CentSchbookEU-Italic", 10.5),
    PDFText(") koniec", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFPageBreak(),
    ]

TEST_DATA_EXTRACT_TEXT5 = [
    PDFText("Pan Jan Kowalski (", "CentSchbookEU-Normal", 10.5),
    PDFText("Dzwo-", "CentSchbookEU-Italic", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFPageBreak(),
    PDFText("nek", "CentSchbookEU-Italic", 10.5),
    PDFText(") koniec", "CentSchbookEU-Normal", 10.5),
    PDFLineBreak(),
    PDFTextBoxBreak(),
    PDFPageBreak(),
    ]


def test_check_extract_textbox_from_middle():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES1, 8)
    assert actual == TEST_DATA_TEXT_BOXES1[7:13]


def test_check_extract_textbox_from_middle_with_breaking_box():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES1, 8, with_breaking_box=True)
    assert actual == TEST_DATA_TEXT_BOXES1[7:14]


def test_check_extract_textbox_from_last_not_closed():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES1, 14)
    assert actual == TEST_DATA_TEXT_BOXES1[14:19]


def test_check_extract_textbox_from_first_not_opened():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES1, 0)
    assert actual == TEST_DATA_TEXT_BOXES1[0:6]


def test_check_extract_textbox_from_index_on_box():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES1, 6)
    assert actual == TEST_DATA_TEXT_BOXES1[0:6]


def test_check_extract_textbox_from_index_on_box_with_breaking_box():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES1, 6, with_breaking_box=True)
    assert actual == TEST_DATA_TEXT_BOXES1[0:7]


def test_check_extract_textbox_empty_if_two_boxes():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES2, 7)
    assert actual == []


def test_check_extract_textbox_nonempty_if_last_is_box():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES2, 10)
    assert actual == TEST_DATA_TEXT_BOXES2[8:10]


def test_check_extract_textbox_empty_if_first_is_box():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES3, 0)
    assert actual == []


def test_check_extract_textbox_nonempty_if_first_is_box_with_breaking_box():
    actual = get_first_text_box_from_index(TEST_DATA_TEXT_BOXES3, 0, with_breaking_box=True)
    assert actual == TEST_DATA_TEXT_BOXES3[0:1]


def test_check_extract_page_from_middle():
    actual = get_first_page_from_index(TEST_DATA_PAGES1, 2)
    assert actual == TEST_DATA_PAGES1[0:8]


def test_check_extract_page_from_middle_with_breaking_box():
    actual = get_first_page_from_index(TEST_DATA_PAGES1, 2, with_breaking_box=True)
    assert actual == TEST_DATA_PAGES1[0:9]
    assert isinstance(actual[-1], PDFPageBreak)


def test_check_extract_page_from_last_wihtout_closing():
    actual = get_first_page_from_index(TEST_DATA_PAGES1, 10)
    assert actual == TEST_DATA_PAGES1[9:13]


def test_check_extract_page_from_last_wihtout_closing_with_breaking_box():
    actual = get_first_page_from_index(TEST_DATA_PAGES1, 10, with_breaking_box=True)
    assert actual == TEST_DATA_PAGES1[9:13]


def test_simple_extract_text():
    actual_text = extract_text_from_parsed_list(TEST_DATA_EXTRACT_TEXT1)
    expected_text = """Pani Katarzyna Pełczyńska-Nałęcz będzie ministrą funduszy i polityki regionalnej
Pan Jan Kowalski

"""
    assert actual_text == expected_text, f"Test extract_text_from_parsed_list TEST_DATA_EXTRACT_TEXT1"


def test_extract_text_with_fixing_word_splits():
    actual_text = extract_text_from_parsed_list(TEST_DATA_EXTRACT_TEXT2)
    expected_text = "Pani Katarzyna Pełczyńska-Nałęcz (Oklaski) będzie ministrą funduszy i polityki regionalnej. Nie mogę na nią spojrzeć, bo nie jest posłanką. Jest pani minister? A, jest. (Oklaski) Jestem naprawdę bardzo usatysfakcjonowany, że będziemy razem pracowali "

    assert actual_text == expected_text, f"Test extract_text_from_parsed_list TEST_DATA_EXTRACT_TEXT2"


def test_simple_extract_text_with_font_styles_tags():
    actual_text = extract_text_from_parsed_list(TEST_DATA_EXTRACT_TEXT3, with_font_styles_tags=True)
    expected_text = """Pani Katarzyna Pełczyńska-Nałęcz będzie ministrą funduszy i polityki regionalnej
Pan Jan Kowalski (<i>Oklaski</i>) <b>koniec</b>

"""
    assert actual_text == expected_text, f"Test extract_text_from_parsed_list TEST_DATA_EXTRACT_TEXT3"


def test_simple_extract_text_with_font_styles_tags_fix_word_split():
    actual_text = extract_text_from_parsed_list(TEST_DATA_EXTRACT_TEXT4, with_font_styles_tags=True)
    expected_text = """Pan Jan Kowalski (<i>Dzwonek</i>) koniec

"""
    assert actual_text == expected_text, f"Test extract_text_from_parsed_list TEST_DATA_EXTRACT_TEXT4"


def test_simple_extract_text_with_font_styles_tags_fix_word_split_on_page_break():
    actual_text = extract_text_from_parsed_list(TEST_DATA_EXTRACT_TEXT5, with_font_styles_tags=True)
    expected_text = """Pan Jan Kowalski (<i>Dzwonek</i>) koniec

"""
    assert actual_text == expected_text, f"Test extract_text_from_parsed_list TEST_DATA_EXTRACT_TEXT5"
