import pytest
from hipisejm.utils.roman_numbers import roman_to_arabic


@pytest.mark.parametrize(
    "in_roman, expected",
    [
        ('X', 10),
        ('x', 10),
    ])
def test_roman_to_arabic(in_roman, expected):
    actual = roman_to_arabic(in_roman)
    assert actual == expected, f"roman_to_arabic({in_roman})"


@pytest.mark.parametrize(
    "in_roman",
    [
        ('XXX'),
        ('C'),
        ('xxx'),
        ('not a roman numeral'),
    ])
def test_roman_to_arabic_unsupported(in_roman):
    actual = roman_to_arabic(in_roman)
    assert actual is None, f"unsupported roman_to_arabic({in_roman})"
