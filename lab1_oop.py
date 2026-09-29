import sys
import math


class BiquadraticEquation:

    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Коэффициент A не должен быть равен нулю.")
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.discriminant < 0:
            return []

        d_sqrt = math.sqrt(self.discriminant)
        y1 = (-self.b + d_sqrt) / (2 * self.a)
        y2 = (-self.b - d_sqrt) / (2 * self.a)

        roots = []
        for y in (y1, y2):
            if y > 0:
                roots.extend((math.sqrt(y), -math.sqrt(y)))
            elif y == 0:
                roots.append(0.0)

        return sorted(set(roots))

    def show_result(self):
        print(f"Дискриминант D = {self.discriminant:g}")
        roots = self.solve()

        if roots:
            print("Действительные корни:")
            for root in roots:
                print(f"x = {root:g}")
        else:
            print("Действительных корней нет.")


def read_coefficient(name, value=None):
    if value is not None:
        try:
            return float(value)
        except ValueError:
            print(f"Некорректное значение {name}: {value!r}.")
            print(f"Введите коэффициент {name} с клавиатуры.")

    while True:
        try:
            return float(input(f"Введите коэффициент {name}: "))
        except ValueError:
            print("Ошибка: коэффициент должен быть действительным числом.")


def main():
    args = sys.argv[1:]
    values = [args[i] if i < len(args) else None for i in range(3)]

    a = read_coefficient("A", values[0])
    while a == 0:
        print("Ошибка: для биквадратного уравнения A не должен быть равен нулю.")
        a = read_coefficient("A")

    b = read_coefficient("B", values[1])
    c = read_coefficient("C", values[2])

    equation = BiquadraticEquation(a, b, c)
    print(f"\nУравнение: {a:g}x^4 + {b:g}x^2 + {c:g} = 0")
    equation.show_result()


if __name__ == "__main__":
    main()
