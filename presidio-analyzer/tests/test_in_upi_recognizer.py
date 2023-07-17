import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import InUpiRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return InUpiRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["IN_UPI"]


@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("jo$n@example", 0, (), (),),
        ("johndoe@upi", 1, (0, 12), 0.75),
        ("my UPI ID is johndoe@upi", 1, (14, 26), 0.9),
        ("Please send money to johndoe@upi for the purchase", 1, (21, 33), 0.8),
        ("UPI: johndoe@upi", 1, (5, 17), 0.6),
        # fmt: on
    ],
)

def test_when_upi_in_text_then_all_upis_found(
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