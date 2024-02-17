from hipisejm.utils.pdfminer_wrapper import clean_fontname, get_fontname_bold_italic_flags
import pytest


@pytest.mark.parametrize(
    "in_fontname, expected_fontname",
    [
        ("DEVWFN+CentSchbookEU-Italic", "CentSchbookEU-Italic"),
        ("DRXWFN+CentSchbookEU-Normal", "CentSchbookEU-Normal"),
        ("SLGIHJ+CentSchbookEU-Italic", "CentSchbookEU-Italic"),
        ("TCXOVH+CentSchbookEU-Bold", "CentSchbookEU-Bold"),
        ("CentSchbookEU-Bold", "CentSchbookEU-Bold"),
        ("ABC", "ABC"),
        ("Times New Roman", "Times New Roman"),
    ])
def test_clean_fontname(in_fontname, expected_fontname):
    actual = clean_fontname(in_fontname)
    assert actual == expected_fontname, f"clean_fontname({in_fontname}) -> {expected_fontname}"


@pytest.mark.parametrize(
    "in_fontname, expected_flags",
    [
        ("DEVWFN+CentSchbookEU-Italic", (False, True)),
        ("DRXWFN+CentSchbookEU-Normal", (False, False)),
        ("SLGIHJ+CentSchbookEU-Italic", (False, True)),
        ("TCXOVH+CentSchbookEU-Bold", (True, False)),
        ("CentSchbookEU-Bold", (True, False)),
        ("ABC", (False, False)),
        ("Times New Roman", (False, False)),
    ])
def test_get_fontname_bold_italic_flags(in_fontname, expected_flags):
    actual = get_fontname_bold_italic_flags(in_fontname)
    assert actual == expected_flags, f"get_fontname_bold_italic_flags({in_fontname}) -> {expected_flags}"
