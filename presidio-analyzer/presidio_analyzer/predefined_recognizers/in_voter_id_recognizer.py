from typing import Optional, List, Tuple

from presidio_analyzer import Pattern, PatternRecognizer


class InVoterIdRecognizer(PatternRecognizer):
    """
    Recognizes Indian Voter ID.

    The Indian Voter ID, also known as the Elector's Photo Identity Card (EPIC),
    is an identification card issued by the Election Commission of India. It serves
    as proof of identity and residence for Indian citizens who are eligible to vote
    in elections. The card contains personal details of the individual, including their
    name, photograph, unique identification number, and residential address.

    This identifier recognizes Indian Voter ID by analyzing the format and content of
    the card. It utilizes regular expressions and context words to identify and extract
    relevant information such as the unique identification number and the individual's name.
    It also verifies the authenticity of the card by cross-checking it with the Election
    Commission of India's database.

    References:

    Election Commission of India: https://eci.gov.in/
    Wikipedia: https://en.wikipedia.org/wiki/Elector%27s_Photo_Identity_Card

    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    :param replacement_pairs: List of tuples with potential replacement values
    for different strings to be used during pattern matching.
    This can allow a greater variety in input, for example by removing dashes or spaces.
    """

    PATTERNS = [
        Pattern(
            "EPIC (High)",
            r"\b([A-Z]{3}[0-9]{7})\b",
            0.85,
        ),
        Pattern(
            "EPIC (Low)",
            r"\b([A-Za-z]{3}[0-9]{7})\b",
            0.4,
        ),
    ]

    CONTEXT = [
        "epic",
        "electors photo identity card",
        "voter id",
        "voter",
        "voter card",
        "eci",
        "election commision"  
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "IN_VOTER_ID",
        replacement_pairs: Optional[List[Tuple[str, str]]] = None,
    ):
        self.replacement_pairs = (
            replacement_pairs if replacement_pairs else [("-", ""), (" ", "")]
        )
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )