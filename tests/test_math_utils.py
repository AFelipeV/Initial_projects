import pytest
from utils import math_utils
import builtins


# -------------------------------
def test_add_numbers_integers():
    assert math_utils.add_numbers(1, 2, 3) == 6


def test_add_numbers_floats():
    assert math_utils.add_numbers(1.5, 2.5, 3.0) == 7.0


def test_add_numbers_empty():
    assert math_utils.add_numbers() == 0


def test_add_numbers_negative():
    assert math_utils.add_numbers(-5, 10, -3) == 2


# -------------------------------
def test_calculate_mean_valid_input(monkeypatch):
    inputs = iter(["2", "4", "6"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    assert math_utils.calculate_mean(3) == 4.0


def test_calculate_mean_with_non_numeric(monkeypatch):
    inputs = iter(["2", "3", "abc"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = math_utils.calculate_mean(3)
    assert result == pytest.approx(5.0/3)


def test_calculate_mean_zero_elements():
    assert math_utils.calculate_mean(0) == 0


# -------------------------------
def test_calculate_median_odd():
    assert math_utils.calculate_median([1, 3, 2]) == 2


def test_calculate_median_even():
    assert math_utils.calculate_median([1, 2, 3, 4]) == 2.5


def test_calculate_median_single():
    assert math_utils.calculate_median([10]) == 10


def test_calculate_median_empty():
    assert math_utils.calculate_median([]) is None


def test_calculate_median_unsorted():
    assert math_utils.calculate_median([7, 1, 3]) == 3


@pytest.mark.parametrize("evaluation_list", [(2.4, 3.6, 7.77), (25, 22.6, 4.7, 6.88)])
def test_calulate_median_floats(evaluation_list):
    assert math_utils.calculate_median(evaluation_list)
