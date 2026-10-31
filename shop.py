
from abc import ABC, abstractmethod
from dataclasses import dataclass


class DiscountStrategy(ABC):
    """Интерфейс алгоритма расчёта скидки."""

    @abstractmethod
    def calculate(self, total: float) -> float:
        """Возвращает итоговую сумму заказа."""


class NoDiscount(DiscountStrategy):
    def calculate(self, total: float) -> float:
        return round(total, 2)


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        if not 0 <= percent <= 100:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 100%")
        self.percent = percent

    def calculate(self, total: float) -> float:
        return round(total * (1 - self.percent / 100), 2)


class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Фиксированная скидка не может быть отрицательной")
        self.amount = amount

    def calculate(self, total: float) -> float:
        return round(max(0, total - self.amount), 2)


@dataclass
class Order:
    items_total: float
    discount_strategy: DiscountStrategy

    def __post_init__(self):
        if self.items_total < 0:
            raise ValueError("Сумма заказа не может быть отрицательной")

    def total(self) -> float:
        return self.discount_strategy.calculate(self.items_total)

    def set_discount_strategy(self, strategy: DiscountStrategy) -> None:
        """Позволяет заменить алгоритм скидки во время выполнения."""
        self.discount_strategy = strategy


def demo() -> None:
    order = Order(1000, NoDiscount())
    print(f"Без скидки: {order.total():.2f} руб.")
    order.set_discount_strategy(PercentageDiscount(10))
    print(f"Скидка 10%: {order.total():.2f} руб.")
    order.set_discount_strategy(FixedDiscount(150))
    print(f"Скидка 150 руб.: {order.total():.2f} руб.")


if __name__ == "__main__":
    demo()
