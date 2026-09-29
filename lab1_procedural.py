import sys
import math


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


def solve_biquadratic(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент A не должен быть равен нулю.")

    d = b * b - 4 * a * c
    print(f"Дискриминант D = {d:g}")

    if d < 0:
        return []

    y1 = (-b + math.sqrt(d)) / (2 * a)
    y2 = (-b - math.sqrt(d)) / (2 * a)

    roots = []
    for y in (y1, y2):
        if y > 0:
            roots.extend((math.sqrt(y), -math.sqrt(y)))
        elif y == 0:
            roots.append(0.0)

    return sorted(set(roots))


def main():
    args = sys.argv[1:]
    values = [args[i] if i < len(args) else None for i in range(3)]

    a = read_coefficient("A", values[0])
    while a == 0:
        print("Ошибка: для биквадратного уравнения A не должен быть равен нулю.")
        a = read_coefficient("A")

    b = read_coefficient("B", values[1])
    c = read_coefficient("C", values[2])

    print(f"\nУравнение: {a:g}x^4 + {b:g}x^2 + {c:g} = 0")

    roots = solve_biquadratic(a, b, c)

    if roots:
        print("Действительные корни:")
        for root in roots:
            print(f"x = {root:g}")
    else:
        print("Действительных корней нет.")


if __name__ == "__main__":
    main()
