import pytest
from hipisejm.utils.polish_dates import convert_polish_date_to_iso, find_polish_dates_in_text


@pytest.mark.parametrize(
    "in_text, expected",
    [
        ('4 marca 2024', '2024-03-04'),
        ('4 MARCA 2024', '2024-03-04'),
        ('14 marca 2024', '2024-03-14'),
        ('4 marca 2024 roku', '2024-03-04'),
        ('14 marca 2024 roku', '2024-03-14'),
    ])
def test_convert_polish_date_to_iso(in_text, expected):
    actual = convert_polish_date_to_iso(in_text)
    assert actual == expected, f"convert_polish_date_to_iso({in_text})"


@pytest.mark.parametrize(
    "in_text, expected",
    [
        ('odbyło się to 4 marca 2024', ['4 marca 2024']),
        ('odbyło się to 4 MARCA 2024', ['4 MARCA 2024']),
        ('odbyło się to 14 marca 2024', ['14 marca 2024']),
        ('4 marca 2024 roku odbyło się', ['4 marca 2024 roku']),
        ('14 marca 2024 roku', ['14 marca 2024 roku']),
        ('14 marca 2024 roku i 15 marca 2024', ['14 marca 2024 roku', '15 marca 2024']),
        ('there is no date here', [])
    ])
def test_find_polish_dates_in_text(in_text, expected):
    actual = find_polish_dates_in_text(in_text)
    assert actual == expected, f"find_polish_dates_in_text({in_text})"
