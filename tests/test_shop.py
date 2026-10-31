"""TDD/unit-тесты и проверка взаимодействия с Mock."""
from unittest.mock import Mock
import pytest

from shop import Order, NoDiscount, PercentageDiscount, FixedDiscount


def test_no_discount_returns_original_total():
    assert Order(1000, NoDiscount()).total() == 1000


@pytest.mark.parametrize(("percent", "expected"), [(10, 900), (25, 750), (100, 0), (0, 1000)])
def test_percentage_discount(percent, expected):
    assert Order(1000, PercentageDiscount(percent)).total() == expected


def test_fixed_discount_does_not_make_total_negative():
    assert Order(100, FixedDiscount(150)).total() == 0


def test_invalid_percentage_is_rejected():
    with pytest.raises(ValueError):
        PercentageDiscount(101)


def test_negative_order_is_rejected():
    with pytest.raises(ValueError):
        Order(-1, NoDiscount())


def test_mock_strategy_is_called_with_order_total():
    strategy = Mock()
    strategy.calculate.return_value = 725.0
    order = Order(800, strategy)

    assert order.total() == 725.0
    strategy.calculate.assert_called_once_with(800)
