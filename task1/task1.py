import argparse


def circle_massiv(n, m):
    if n <= 0 or m <= 0:
        raise ValueError("Длина массива и шаг должны быть положительными числами")
    if m > n:
        raise ValueError("Длина шага не может быть больше самого массива")

    lst = list(range(1, n + 1))
    circle = lst.copy()
    circle_m = []
    for i in circle:
        circle_m.append(circle[:m])
        circle = circle[m - 1 :] + circle[: m - 1]
        if circle_m[-1][-1] == lst[0]:
            break
    answer = ""
    for el in circle_m:
        answer += str(el[0])
    return answer


def interactive_input():
    n1 = int(input("Введите длину первого массива: "))
    m1 = int(input("Введите интервал для первого массива: "))
    n2 = int(input("Введите длину второго массива: "))
    m2 = int(input("Введите интервал для второго массива: "))
    return n1, m1, n2, m2


def main():
    parser = argparse.ArgumentParser(
        description="Программа позваляет вычислить шаг двух круговых массивов",
        epilog="Примеры:\npython task1.py --n1 5 --m1 3 --n2 4 --m2 2\npython task1.py (для интерактивного режима)\n❗️ Числа для массива и шаг массива должны быть положительными и целыми числами.\n❗️ Длина шага должна быть меньше самого массива",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--n1", type=int, help="Введите длину первого массива")
    parser.add_argument("--m1", type=int, help="Введите шаг для первого массива")
    parser.add_argument("--n2", type=int, help="Введите длину второго массива")
    parser.add_argument("--m2", type=int, help="Введите шаг для второго массива")

    args = parser.parse_args()

    try:
        if all([args.n1, args.m1, args.n2, args.m2]): #Если введены все аргументы запускает режим командной строки
            print(
                "\nРежим командной строки",
            )
            n1, m1, n2, m2 = args.n1, args.m1, args.n2, args.m2

        else:
            print("\nИнтерактивный режим")
            n1, m1, n2, m2 = interactive_input()

        path1 = circle_massiv(n1, m1)
        path2 = circle_massiv(n2, m2)
        result = path1 + path2
        print(f"\nПуть для массива {n1} с шагом {m1}: {path1}")
        print(f"Путь для массива {n2} с шагом {m2}: {path2}")
        print(f"Общий результат: {result}")

    except ValueError as e:
        print(f"❌ Ошибка: {e}")
    except Exception as e:
        print(f"⚠️ Неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()
