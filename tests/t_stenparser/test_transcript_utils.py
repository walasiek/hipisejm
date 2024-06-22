import pytest
from hipisejm.stenparser.transcript import SessionSpeech, SpeechInterruption, SpeechReaction
from hipisejm.stenparser.transcript_utils import get_utt_text, get_speaker_for_utt


@pytest.mark.parametrize(
    "utt, speech, expected_speaker",
    [
        ("Poniedziałek: Ja", SessionSpeech("Witold Gombrowicz"), "Witold Gombrowicz"),
        (SpeechReaction("Uderzają buch bachem"), SessionSpeech("Witold Gombrowicz"), None),
        (SpeechInterruption("Henryk Sienkiewicz", "Ale jak to DRUGORZĘDNY?"), SessionSpeech("Witold Gombrowicz"), "Henryk Sienkiewicz"),
    ]
    )
def test_get_speaker_for_utt(utt, speech, expected_speaker):
    actual_speaker = get_speaker_for_utt(utt, speech)
    assert actual_speaker == expected_speaker, f"check get_speaker_for_utt for ({utt})"


@pytest.mark.parametrize(
    "utt, expected_text",
    [
        ("Poniedziałek: Ja", "Poniedziałek: Ja"),
        (SpeechReaction("Uderzają buch bachem"), "Uderzają buch bachem"),
        (SpeechInterruption("Henryk Sienkiewicz", "Ale jak to DRUGORZĘDNY?"), "Ale jak to DRUGORZĘDNY?"),
    ]
    )
def test_get_utt_text(utt, expected_text):
    actual_text = get_utt_text(utt)
    assert actual_text == expected_text, f"check get_utt_text for ({utt})"
