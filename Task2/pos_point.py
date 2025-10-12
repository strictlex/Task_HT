# Считываем радиус и координаты окружности из file1.txt
with open(
    "file1.txt", "r", encoding="utf-8"
) as f1:
    x0, y0 = [int(i) for i in f1.readline().split()]
    r = int(f1.readline()) ** 2
# Считываем координаты точек из file2.txt
with open(
    "file2.txt", "r", encoding="utf-8"
) as f2:
    cnt_point = len(f2.readlines())
    f2.seek(0)
    for el in f2:
        x, y = [int(i) for i in el.split()]
        position = (x - x0) ** 2 + (y - y0) ** 2
        dct_true = {r == position: 0, r > position: 1, r < position: 2}
        print(dct_true[True])
