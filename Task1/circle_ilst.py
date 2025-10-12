n, m = int(input("Введите длину кругового массива: ")), int(
    input("Введите интервал длины для массива: ")
)
circle_list = list(range(1, n + 1))
result = []

for el in range(len(circle_list)):
    result.extend(circle_list[:m])
    circle_list = circle_list[m - 1 :] + circle_list[: m - 1]
    if result[-1] == result[0]:
        break
track = ''.join([str(i) for i in result[::m]])
print(f"Полученный путь: {track}")

