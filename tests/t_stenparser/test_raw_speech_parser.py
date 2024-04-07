import os
import pytest
from hipisejm.stenparser.raw_speech_parser import RawSpeechParser
import xml.etree.ElementTree as ET
from xml.dom import minidom


def to_xml_test_wrapper(session_speech, expected_parsed_xml):
    root_tag = ET.Element("root")

    session_speech.to_xml(root_tag)
    tree_str = ET.tostring(root_tag, 'utf-8')
    pretty_xml = minidom.parseString(tree_str).toprettyxml(indent="")

    expected_wrapped = '<?xml version="1.0" ?>' + f"\n<root>\n{expected_parsed_xml}\n</root>\n"
    assert pretty_xml == expected_wrapped


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku</utt>
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję\nPanie\n\n\nMarszałku",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku</utt>
</speech>"""),
    ])
def test_simple_parse_no_interruptions(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)
    to_xml_test_wrapper(actual_speech, expected_parsed_xml)


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Oklaski</i>) za sprawne prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku</utt>
<utt t="reaction">Oklaski</utt>
<utt t="norm">za sprawne prowadzenie obrad.</utt>
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Oklaski</i>) za sprawne prowadzenie (<i>Wesołość na sali, gwar</i>)obrad.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku</utt>
<utt t="reaction">Oklaski</utt>
<utt t="norm">za sprawne prowadzenie</utt>
<utt t="reaction">Wesołość na sali, gwar</utt>
<utt t="norm">obrad.</utt>
</speech>"""),
    ])
def test_parse_with_reactions(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)
    to_xml_test_wrapper(actual_speech, expected_parsed_xml)


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Głos z sali</i>: Hańba!) za sprawne prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku</utt>
<utt t="interrupt" by="Głos z sali">Hańba!</utt>
<utt t="norm">za sprawne prowadzenie obrad.</utt>
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Głos z sali:</i>Hańba!) za sprawne prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku</utt>
<utt t="interrupt" by="Głos z sali">Hańba!</utt>
<utt t="norm">za sprawne prowadzenie obrad.</utt>
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Głos z sali:</i> Hańba!) za sprawne prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku</utt>
<utt t="interrupt" by="Głos z sali">Hańba!</utt>
<utt t="norm">za sprawne prowadzenie obrad.</utt>
</speech>"""),
    ])
def test_parse_with_interruption(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)
    to_xml_test_wrapper(actual_speech, expected_parsed_xml)


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku (<i>Oklaski</i>) za sprawne (<i>Głos z sali</i>: Hańba!) prowadzenie obrad.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku</utt>
<utt t="reaction">Oklaski</utt>
<utt t="norm">za sprawne</utt>
<utt t="interrupt" by="Głos z sali">Hańba!</utt>
<utt t="norm">prowadzenie obrad.</utt>
</speech>"""),
    ])
def test_parse_reactions_and_interruptions(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)
    to_xml_test_wrapper(actual_speech, expected_parsed_xml)


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        (
            "Jan Kowalski",
            "Dziękuję Panie <b>Marszałku</b>.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku.</utt>
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie <i>Marszałku</i>.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku.</utt>
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie <i><b>Marszałku</b></i>.",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku.</utt>
</speech>"""),
        (
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<b>druk nr 123</b>)",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku. (druk nr 123)</utt>
</speech>"""),
    ])
def test_parse_with_other_tags_which_should_be_ignored(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)
    to_xml_test_wrapper(actual_speech, expected_parsed_xml)


@pytest.mark.parametrize(
    "input_speaker, input_raw_speech, expected_parsed_xml",
    [
        ( # 02_b_ksiazka.pdf: not whole parens text is in italics
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<i>Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym </i>mikrofonie)",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku.</utt>
<utt t="reaction">Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie</utt>
</speech>"""),
        ( # 02_b_ksiazka.pdf: not whole parens text is in italics
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<i>Poseł Grzegorz </i>Braun: W trybie sprostowania. Zostało wymienione moje nazwisko w kontekście niewątpliwie zmanipulowanym, krzywdzącym.)",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku.</utt>
<utt t="interrupt" by="Poseł Grzegorz Braun">W trybie sprostowania. Zostało wymienione moje nazwisko w kontekście niewątpliwie zmanipulowanym, krzywdzącym.</utt>
</speech>"""),
        ( # 01_a_ksiazka_bis.pdf: multiple italics for reaction
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<i>Oklaski</i>, <i>część posłów wstaje</i>)",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku.</utt>
<utt t="reaction">Oklaski, część posłów wstaje</utt>
</speech>"""),
        ( # 01_a_ksiazka_bis.pdf: error in source file, unable to fix
            "Jan Kowalski",
            "Dziękuję Panie Marszałku. (<i>Głos z sali</i>: Szanowny panie marszałku, bardzo dziękujemy za piękne reprezentowanie nas, za sprawne prowadzenie posiedzenia.Szymon, jeszcze raz gratulacje. Życzę ci powodzenia. (<i>Oklaski</i>)",
            """<speech speaker="Jan Kowalski">
<utt t="norm">Dziękuję Panie Marszałku.</utt>
</speech>"""), # all in parens is lost (unable to recover automatically)
    ])
def test_parse_tricky_cases_from_real_examples(input_speaker, input_raw_speech, expected_parsed_xml):
    raw_speech_parser = RawSpeechParser()
    actual_speech = raw_speech_parser.parse_raw_speech(input_speaker, input_raw_speech)
    to_xml_test_wrapper(actual_speech, expected_parsed_xml)
