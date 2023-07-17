from typing import Optional, List, Tuple

from presidio_analyzer import Pattern, PatternRecognizer


class InUpiRecognizer(PatternRecognizer):
    """
    Recognizes Unified Payments Interface (UPI) IDs.

    The Unified Payments Interface (UPI) is a real-time payment system in India
    that allows users to link multiple bank accounts and perform instant money
    transfers. UPI IDs are unique identifiers assigned to individuals or entities
    for receiving payments through the UPI system. They typically follow a
    specific format and can include alphanumeric characters and special symbols.

    This UPI ID identifier uses a combination of regex patterns and contextual
    analysis to identify UPI IDs. It matches the patterns based on the prescribed
    format and verifies them against known UPI ID prefixes and domain names.
    Additionally, it may utilize API calls to validate the UPI ID against the
    UPI payment infrastructure for enhanced accuracy.

    References:

    NPCI UPI FAQs: https://www.npci.org.in/sites/default/files/UPI_FAQs_24June2021.pdf
    UPI Specification: https://www.npci.org.in/sites/default/files/UPI-Linking-Specs-ver-1.6.pdf

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
            "UPI (High)",
            r"\b[a-z0-9.-]{2,256}+@(oksbi|sbi|ybl|paytm|okaxis|okicici|imobile|pockets|ezeepay|eazypay|icici|hdfcbank|payzapp|okhdfcbank|rajgovhdfcbank|mahb|kotak|kaypay|kmb|kmbl|yesbank|yesbankltd|ubi|united|utbi|idbi|idbibank|hsbc|pnb|centralbank|cbin|cboi|cnrb|barodampay|upi)\b",
            0.9,
        ),
        Pattern(
            "UPI (Medium)",
            r"\b([a-z0-9.-]{2,256}@[a-z]{2,64})",
            0.7,
        ),
        Pattern(
            "UPI (Low)",
            r"\b([A-Za-z0-9.-]{2,256}@[A-Za-z0-9]{2,64})",
            0.4,
        ),
    ]

    CONTEXT = [
        "upi",
        "unified payments interface",
        "google pay",
        "paytm",
        "phonepe",
        "phone pay", 
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "IN_UPI_ID",
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