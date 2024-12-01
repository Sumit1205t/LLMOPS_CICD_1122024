import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator.calculator import Calculator
import math
import pytest

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()

    # Basic Operations Tests
    @pytest.mark.parametrize("x, y, expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (999999, 1, 1000000),
        (-5.5, 2.2, -3.3),
    ])
    def test_addition(self, calculator, x, y, expected):
        assert math.isclose(calculator.add(x, y), expected, rel_tol=1e-9)

    @pytest.mark.parametrize("x, y, expected", [
        (5, 3, 2),
        (1, 1, 0),
        (0, 5, -5),
        (-5, -3, -2),
        (10.5, 3.2, 7.3),
    ])
    def test_subtraction(self, calculator, x, y, expected):
        assert math.isclose(calculator.subtract(x, y), expected, rel_tol=1e-9)

    # ... More test cases would follow ...

    # Edge Cases
    def test_division_by_zero(self, calculator):
        with pytest.raises(ValueError):
            calculator.divide(1, 0)

    def test_negative_logarithm(self, calculator):
        with pytest.raises(ValueError):
            calculator.logarithm(-1)

    def test_negative_square_root(self, calculator):
        with pytest.raises(ValueError):
            calculator.square_root(-1) 