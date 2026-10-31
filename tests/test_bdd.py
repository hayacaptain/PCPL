"""BDD-сценарии на pytest-bdd, соответствующие features/discount.feature."""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from shop import Order, PercentageDiscount, FixedDiscount

scenarios("../features/discount.feature")


@given(parsers.parse("сумма заказа составляет {amount:d} рублей"), target_fixture="order_amount")
def order_amount(amount):
    return amount


@when(parsers.parse("применяется скидка {percent:d} процентов"), target_fixture="result")
def apply_percentage(order_amount, percent):
    return Order(order_amount, PercentageDiscount(percent)).total()


@when(parsers.parse("применяется фиксированная скидка {discount:d} рублей"), target_fixture="result")
def apply_fixed(order_amount, discount):
    return Order(order_amount, FixedDiscount(discount)).total()


@then(parsers.parse("итоговая сумма заказа равна {expected:d} рублей"))
def check_result(result, expected):
    assert result == expected
