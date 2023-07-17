import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import InVoterIdRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return InVoterIdRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["IN_VOTER_ID"]


@pytest.mark.parametrize(
    "text, expected_len, expected_position, expected_score",
    [
        # fmt: off
        ("ABCD1234567", 1, (0, 11), 0.9),
        ("XYZW9876543", 1, (0, 11), 0.75),
        ("PQRV12345", 0, (), (),),
        ("My voter ID is EFGH5678901 with some additional text", 1, (15, 26), 0.8),
        # fmt: on
    ],
)

def test_when_voterid_in_text_then_all_voterids_found(
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