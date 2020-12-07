import pytest
from Year2019.Task1 import SpaceshipMass


@pytest.mark.parametrize("input, output", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_file1_method1(input, output):
    assert SpaceshipMass.Mass().getMass(input) == output, "test failed"
