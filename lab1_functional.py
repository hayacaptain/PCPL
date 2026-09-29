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


def solve_with_pattern(a, b, c):
    """Паттерн матчинг"""
    match a, b, c:
        case (a, b, c) if a == 0:
            raise ValueError("Коэффициент A не должен быть равен нулю.")
        case (a, b, c):
            d = b ** 2 - 4 * a * c
            print(f"Дискриминант D = {d:g}")

            match d:
                case d if d < 0:
                    return []
                case _:
                    sqrt_d = math.sqrt(d)
                    y_values = (
                        (-b + sqrt_d) / (2 * a),
                        (-b - sqrt_d) / (2 * a),
                    )

                    roots = []
                    for y in y_values:
                        match y:
                            case y if y > 0:
                                roots.extend((math.sqrt(y), -math.sqrt(y)))
                            case 0:
                                roots.append(0.0)
                            case _:
                                pass

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
    roots = solve_with_pattern(a, b, c)

    if roots:
        print("Действительные корни:")
        for root in roots:
            print(f"x = {root:g}")
    else:
        print("Действительных корней нет.")


if __name__ == "__main__":
    main()
