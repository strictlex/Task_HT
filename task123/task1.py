def circle_massiv(n, m):
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


n1 = int(input("Введите длину первого массива: "))
m1 = int(input("Введите интервал для первого массива: "))
n2 = int(input("Введите длину второго массива: "))
m2 = int(input("Введите интервал для второго массива: "))

n1m1 = circle_massiv(n1, m1)
n2m2 = circle_massiv(n2, m2)

print(n1m1 + n2m2)
