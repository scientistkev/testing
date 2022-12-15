"""An example of a test module in pytest"""

from ls24_module import total

def test_total_empty() -> None:
    """Total of empty list should be 0.0"""
    assert total([]) == 0.0


def test_total_single_value() -> None:
    """Total of a single item list should be the first item's value"""
    assert total([110.0]) == 110.0