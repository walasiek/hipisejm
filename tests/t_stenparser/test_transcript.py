import pytest
import os
from hipisejm.stenparser.transcript import SessionTranscript, SpeechInterruption, SpeechReaction


SAMPLE_PARSED_FILEPATH = os.path.join("resources", "test_data", "parsed-01_j_ksiazka-part.xml")


def test_01_j_ksiazka():
    transcript = SessionTranscript()
    transcript.load_from_xml(SAMPLE_PARSED_FILEPATH)

    # check metadata
    assert transcript.session_no == 1, "session_no"
    assert transcript.term_no == 10, "term_no"
    assert transcript.session_date == "2023-12-12", "session_date"

    # check session officials
    session_officials = transcript.session_officials
    officials_list = session_officials.officials_list
    assert officials_list[0] == ('speaker', 'Szymon Hołownia'), f"session officials 0 from file: {SAMPLE_PDF_FILEPATH}"
    assert officials_list[1] == ('vice_speaker', 'Monika Wielichowska'), f"session officials 1 from file: {SAMPLE_PDF_FILEPATH}"
    assert officials_list[2] == ('vice_speaker', 'Włodzimierz Czarzasty'), f"session officials 2 from file: {SAMPLE_PDF_FILEPATH}"
    assert officials_list[3] == ('vice_speaker', 'Krzysztof Bosak'), f"session officials 3 from file: {SAMPLE_PDF_FILEPATH}"
    assert officials_list[4] == ('vice_speaker', 'Piotr Zgorzelski'), f"session officials 4 from file: {SAMPLE_PDF_FILEPATH}"
    assert officials_list[5] == ('vice_speaker', 'Dorota Niedziela'), f"session officials 5 from file: {SAMPLE_PDF_FILEPATH}"

    session_content = transcript.session_content

    # check first speech
    speech0 = session_content[0]
    assert "Marszałek Szymon Hołownia" == speech0.speaker, f"{SAMPLE_PDF_FILEPATH}: first speech, who is speaker"
    assert "Szanowni Państwo! Opóźniam trochę wznowienie posiedzenia, dlatego że widzę, jak długa kolejka posłów chcących zapisać się do pytań po exposé ustawiła się tutaj." in speech0.content[0], f"{SAMPLE_PDF_FILEPATH}: first speech, first sentence"

    assert isinstance(speech0.content[1], SpeechReaction), f"{SAMPLE_PDF_FILEPATH}: first speech, second -> reaction"
    assert speech0.content[1].reaction_text == "Wypowiedź poza mikrofonem", f"{SAMPLE_PDF_FILEPATH}: first speech, second -> reaction"

    assert isinstance(speech0.content[5], SpeechInterruption), f"{SAMPLE_PDF_FILEPATH}: first speech, sixth -> interruption"
    assert speech0.content[5].interrupted_by_speaker == "Głos z sali", f"{SAMPLE_PDF_FILEPATH}: first speech, sixth -> interruption (interrupted_by_speaker)"
    assert speech0.content[5].text == "Sprzeciw!", f"{SAMPLE_PDF_FILEPATH}: first speech, sixth -> interruption (text)"
