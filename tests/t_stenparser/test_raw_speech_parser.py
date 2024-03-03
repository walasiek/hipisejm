import os
import pytest
from hipisejm.stenparser.raw_speech_parser import RawSpeechParser


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję\nPanie\n\n\nMarszałku",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku
</speech>"""),
    ])
def test_simple_parse_no_interruptions(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)

    assert actual_speech.to_xml() == expected_parsed_xml


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Oklaski</i>) za sprawne prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku
<reaction>Oklaski</reaction>
za sprawne prowadzenie obrad.
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Oklaski</i>) za sprawne prowadzenie (<i>Wesołość na sali, gwar</i>)obrad.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku
<reaction>Oklaski</reaction>
za sprawne prowadzenie
<reaction>Wesołość na sali, gwar</reaction>
obrad.
</speech>"""),
    ])
def test_parse_with_reactions(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)

    assert actual_speech.to_xml() == expected_parsed_xml


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Głos z sali</i>: Hańba!) za sprawne prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku
<interruption by="Głos z sali">Hańba!</interruption>
za sprawne prowadzenie obrad.
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Głos z sali:</i>Hańba!) za sprawne prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku
<interruption by="Głos z sali">Hańba!</interruption>
za sprawne prowadzenie obrad.
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Głos z sali:</i> Hańba!) za sprawne prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku
<interruption by="Głos z sali">Hańba!</interruption>
za sprawne prowadzenie obrad.
</speech>"""),
    ])
def test_parse_with_interruption(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)

    assert actual_speech.to_xml() == expected_parsed_xml


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Oklaski</i>) za sprawne (<i>Głos z sali</i>: Hańba!) prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku
<reaction>Oklaski</reaction>
za sprawne
<interruption by="Głos z sali">Hańba!</interruption>
prowadzenie obrad.
</speech>"""),
    ])
def test_parse_reactions_and_interruptions(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)

    assert actual_speech.to_xml() == expected_parsed_xml


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie <b>Marszałku</b>.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku.
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie <i>Marszałku</i>.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku.
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie <i><b>Marszałku</b></i>.",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku.
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<b>druk nr 123</b>)",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku. (druk nr 123)
</speech>"""),
    ])
def test_parse_with_other_tags_which_should_be_ignored(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)

    assert actual_speech.to_xml() == expected_parsed_xml


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        ( # 02_b_ksiazka.pdf: not whole parens text is in italics
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<i>Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym </i>mikrofonie)",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku.
<reaction>Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie</reaction>
</speech>"""),
        ( # 02_b_ksiazka.pdf: not whole parens text is in italics
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<i>Poseł Grzegorz </i>Braun: W trybie sprostowania. Zostało wymienione moje nazwisko w kontekście niewątpliwie zmanipulowanym, krzywdzącym.)",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku.
<interruption by="Poseł Grzegorz Braun">W trybie sprostowania. Zostało wymienione moje nazwisko w kontekście niewątpliwie zmanipulowanym, krzywdzącym.</interruption>
</speech>"""),
        ( # 01_a_ksiazka_bis.pdf: multiple italics for reaction
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<i>Oklaski</i>, <i>część posłów wstaje</i>)",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku.
<reaction>Oklaski, część posłów wstaje</reaction>
</speech>"""),
        ( # 01_a_ksiazka_bis.pdf: error in source file, unable to fix
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<i>Głos z sali</i>: Szanowny panie marszałku, bardzo dziękujemy za piękne reprezentowanie nas, za sprawne prowadzenie posiedzenia.Szymon, jeszcze raz gratulacje. Życzę ci powodzenia. (<i>Oklaski</i>)",
            """<speech speaker="Jan Kowalski">
Dziękuję Panie Marszałku.
</speech>"""), # all in parens is lost (unable to recover automatically)
    ])
def test_parse_tricky_cases_from_real_examples(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)

    assert actual_speech.to_xml() == expected_parsed_xml
