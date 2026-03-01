
import math
import pytest

from src.python import calculator

# During the demo, ask Copilot to generate more tests and parametrize them.

def test_add_basic():
    # Replace with a real call after implementing add()
    # Expect 2 + 3 == 5
    with pytest.raises(AttributeError):
        _ = calculator.add(2, 3)  # This will fail until add exists; great for the demo


def test_mean_empty_raises():
    # After implementing mean(), this should raise ValueError for empty input
    with pytest.raises(ValueError):
        calculator.mean([])
