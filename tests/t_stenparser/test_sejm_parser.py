import os
from hipisejm.stenparser.sejm_parser import SejmParser
from hipisejm.stenparser.transcript import SpeechInterruption, SpeechReaction


SAMPLE_PDF_FILEPATH = os.path.join("resources", "test_data", "01_j_ksiazka.pdf")


def test_01_j_ksiazka():
    parser = SejmParser()
    assert parser is not None, "SejmParser created and not None"
    assert os.path.isfile(SAMPLE_PDF_FILEPATH), f"File: {SAMPLE_PDF_FILEPATH} exists"

    # start parsing
    transcript = parser.parse_file(SAMPLE_PDF_FILEPATH)

    assert parser.number_of_pages == 132, f"number of pages in the file: {SAMPLE_PDF_FILEPATH}"

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

    # last speech should not contain "Teksty wystąpień niewygłoszonych w załączniku"
    last_speech = session_content[-1]
    last_speech_bare_content = last_speech.get_bare_content()

    assert "Na tym zakończyliśmy oświadczenia poselskie" in last_speech_bare_content, "last_speech check is correct (text)"
    assert last_speech.speaker == "Wicemarszałek Włodzimierz Czarzasty", "last_speech check is correct (speaker)"
    assert "*)" not in last_speech_bare_content, "last_speech check is correct (no *) in content)"
    assert "Teksty wystąpień" not in last_speech_bare_content, "last_speech check is correct (no Teksty wystąpień in content)"

    # spaces should not be lost if line break is introduced
    speech71 = session_content[71]
    assert "Bardzo dziękuję, panie pośle. Marek Jakubiak, Kukiz’15. Zapraszam." in speech71.get_bare_content(), "spaces should not be lost after newline"

    # Some tricky cases
    # tricky_case1: reaction in two lines in PDF
    # "To nie jest sprawa, panie marszałku, jak był pan łaskaw to dziś podsumować, prywatnego chamstwa [...]"
    speech_braun_tetrycy = session_content[7]
    assert "To nie jest sprawa, panie marszałku, jak był pan łaskaw" in speech_braun_tetrycy.get_bare_content(), "check tricky_case1"
    long_reaction = speech_braun_tetrycy.content[4]
    assert isinstance(long_reaction, SpeechReaction), "check tricky_case1"
    assert long_reaction.reaction_text == "Marszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie", "check tricky_case1"

    # tricky_case2: speaker name in two lines in PDF
    # "Panie Marszałku! Panie Posłanki! Panowie Posłowie! Czcigodni Goście! 16 lat temu [...]"
    speech_first_tusk = session_content[11]
    assert "Panie Marszałku! Panie Posłanki! Panowie Posłowie! Czcigodni Goście! 16 lat temu" in speech_first_tusk.get_bare_content(), "check tricky_case2"
    assert speech_first_tusk.speaker == "Prezes Rady Ministrów Donald Tusk", "check tricky_case2"

    # tricky_case3: 'Oklaski' in two lines + Speaker name repeated on new page
    # "Jeszcze jedno – bardzo dziękuję, panie marszałku – wyjaśnienie, bo doszło tu do jakiegoś nieporozumienia [...]"
    speech_first_czarnek = session_content[384]
    assert "Jeszcze jedno – bardzo dziękuję, panie marszałku – wyjaśnienie," in speech_first_czarnek.get_bare_content(), "check tricky_case3"
    assert "A wy z kolei dzisiaj powiedzieliście, że chcecie kontynuować pytania, więc zastanówcie się" in speech_first_czarnek.get_bare_content(), "check tricky_case3"

    split_oklaski_reaction = speech_first_czarnek.content[3]
    assert isinstance(split_oklaski_reaction, SpeechReaction), "check tricky_case3"
    assert split_oklaski_reaction.reaction_text == "Oklaski", "check tricky_case3"
