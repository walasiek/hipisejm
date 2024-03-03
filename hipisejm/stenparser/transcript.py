from collections import defaultdict


class SessionOfficials:
    """
    This class represents officials of the sessions like Marszałek, Marszałek senior and Wicemarszałek
    """
    def __init__(self):
        self.officials_list = []
        self.role_to_officials = defaultdict(list)

    def add_new(self, role_name, person_name):
        new_entry = (role_name, person_name)
        self.role_to_officials[role_name].append(new_entry)
        self.officials_list.append(new_entry)

    def __str__(self):
        chunks = ["Session officials:"]
        for entry in self.officials_list:
            chunks.append(f"  {entry[0]}: {entry[1]}")
        return "\n".join(chunks)

    def to_xml(self) -> str:
        chunks = []
        for official in self.officials_list:
            chunk = '<official title="' + official[0] + '" name="' + official[1] + '"/>'
            chunks.append(chunk)

        return "\n".join(chunks)

    def get_by_role(self, role_name: str):
        """
        Returns list of entries for persons with given role on the session.
        If there is no such role during the session then returns empty list.
        """
        return self.role_to_officials.get(role_name, [])


class SpeechReaction:
    """
    Reactions are spontanous interruptions of the speech without particular speaker
    Can be something like appluase, noise, laugh, etc...
    """
    def __init__(self, reaction_text: str):
        self.reaction_text = reaction_text

    def to_xml(self) -> str:
        return f"<reaction>{self.reaction_text}</reaction>"


class SpeechInterruption:
    """
    Interruptions are from the audience and particular speaker
    Sometimes the speaker is unknown ("Głos z sali") or refers to multiple persons speaking
    """
    def __init__(self, interrupted_by_speaker: str, text: str):
        self.interrupted_by_speaker = interrupted_by_speaker
        self.text = text

    def to_xml(self) -> str:
        return '<interruption by="' + self.interrupted_by_speaker + '">' + f"{self.text}</interruption>"


class SessionSpeech:
    """
    Speech is the one uninterrupted sequence of utterance of the given person.
    Speech consists of:
    - utterances of the speaker
    - intteruptions from the audience
    - reactions
    """
    def __init__(self, speaker: str):
        self.speaker = speaker
        self.content = []
        # memoization of the bare speech without interruptions
        self.bare_content = None

    def add_speech_text(self, text: str):
        self.bare_content = None
        self.content.append(text)

    def get_bare_content(self):
        if self.bare_content is None:
            chunks = []
            for cont in self.content:
                if isinstance(cont, str):
                    chunks.append(cont)
            self.bare_content = "".join(chunks)
        return self.bare_content

    def add_interruption(self, interruption: SpeechInterruption):
        self.content.append(interruption)

    def add_reaction(self, reaction: SpeechReaction):
        self.content.append(reaction)

    def to_xml(self) -> str:
        result = []

        result.append('<speech speaker="' + self.speaker + '">')
        for entry in self.content:
            if isinstance(entry, str):
                result.append(entry)
            else:
                result.append(entry.to_xml())
        result.append("</speech>")

        return "\n".join(result)


class SessionTranscript:
    """
    Session Transcript stores all speeches from the given session.
    """
    def __init__(self):
        self.session_officials = SessionOfficials()
        self.session_content = []

    def dump_to_xml(self, filepath: str= None):
        with open(filepath, "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write("""<session xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:noNamespaceSchemaLocation="hipisejm-transcript-schema.xsd">""")
            f.write("\n")

            f.write('<session_officials>\n')
            f.write(self.session_officials.to_xml())
            f.write("\n")
            f.write('</session_officials>\n')

            f.write('<content>\n')
            self._dump_session_content_to_xml(f)
            f.write('</content>\n')

            f.write('</session>\n')
        # TODO
        pass

    def load_from_xml(self, filepath: str):
        # TODO unimplemented (yet)
        pass

    def __str__(self):
        chunks = []
        chunks.append(str(self.session_officials))
        return "\n".join(chunks)

    def add_speech(self, speech: SessionSpeech):
        self.session_content.append(speech)

    def _dump_officials_to_xml(self, f):
        for session_official in self.session_officials:
            f.write(session_official.to_xml())
            f.write("\n")

    def _dump_session_content_to_xml(self, f):
        for speech in self.session_content:
            f.write(speech.to_xml())
            f.write("\n")
