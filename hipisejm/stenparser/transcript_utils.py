from typing import Union, List, Optional
from hipisejm.stenparser.transcript import SessionTranscript, SpeechReaction, SpeechInterruption, SessionSpeech


def get_speaker_for_utt(utt: Union[str, SpeechReaction, SpeechInterruption], speech: SessionSpeech) -> Optional[str]:
    """
    Gets speaker for <utt> object of any type (if known).
    Returns None if speaker is not known (e.g. for reaction).
    """
    if isinstance(utt, str):
        return speech.speaker
    elif isinstance(utt, SpeechReaction):
        return None
    elif isinstance(utt, SpeechInterruption):
        return utt.interrupted_by_speaker
    else:
        raise ValueError(f"Unknown object type utt: {utt}")


def get_utt_text(utt: Union[str, SpeechInterruption, SpeechReaction]) -> str:
    """
    Returns text for <utt> object of any type.
    """
    if isinstance(utt, str):
        return utt
    elif isinstance(utt, SpeechReaction):
        return utt.reaction_text
    elif isinstance(utt, SpeechInterruption):
        return utt.text
    else:
        raise ValueError(f"Unknown object type utt in: {utt}")
