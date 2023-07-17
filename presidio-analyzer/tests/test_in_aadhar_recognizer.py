import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import InAadharRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return InAadharRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["IN_AADHAR"]



@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("4234 5678 9012", 1, (0, 14), 0.6),
        ("Aadhaar number: 9876 5432 1098", 1, (14, 32), 0.9),
        ("My Aadhaar is 8765 4321 0987", 1, (11, 29), 0.8),
        ("1234 5678", 0, (), (),),
        ("Aadhaar: 4321 8765 0987 with other text", 1, (9, 27), 0.85),
        # fmt: on
    ],
)
def test_when_aadhar_in_text_then_all_aadhars_found(
    text,
    expected_len,
    expected_position,
    expected_score,
    recognizer,
    entities,
):
    results = recognizer.analyze(text, entities)
    print(results)

    assert len(results) == expected_len
    if results:
        assert_result(
            results[0],
            entities[0],
            expected_position[0],
            expected_position[1],
            expected_score,
        )