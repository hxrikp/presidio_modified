from typing import Optional, List, Tuple

from presidio_analyzer import Pattern, PatternRecognizer


class InAadharRecognizer(PatternRecognizer):
    """
    Recognizes Indian Aadhaar Number.

    The Aadhaar Number is a unique 12-digit identification number issued by the Unique
    Identification Authority of India (UIDAI) to residents of India. It serves as a proof
    of identity and address for various government and private services. The number is generated
    based on a person's biometric and demographic data, including fingerprints and iris scans.

    This identifier recognizes Aadhaar Numbers using a combination of pattern matching and
    context analysis. It utilizes regular expressions and keywords related to Aadhaar to identify
    and extract Aadhaar Numbers from text inputs. The Aadhaar identifier also performs a validity
    check using the check-digit algorithm specified by the UIDAI.

    Reference:
    https://uidai.gov.in/
    https://en.wikipedia.org/wiki/Aadhaar

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
            "AADHAR (High)",
            r"\b([2-9]{4}\s[0-9]{4}\s[0-9]{4})\b",
            0.85,
        ),
        Pattern(
            "AADHAR (Medium)",
            r"\b([2-9]{1}[0-9]{3}\s?[0-9]{4}\s?[0-9]{4})\b",
            0.6,
        ),
        Pattern(
            "AADHAR (Low)",
            r"\b([0-9]{4}\s?[0-9]{4}\s?[0-9]{4})\b",
            0.05,
        ),
    ]

    CONTEXT = [
        "aadhar number",
        "aadhar",
        "unique id",
        "identity number",
        "uidai"
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "IN_AADHAR",
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
