from hipisejm.utils.pdfminer_wrapper import clean_fontname
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
