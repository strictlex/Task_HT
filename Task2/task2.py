# учитывая, что в задаче не указан угол наклона элипса относительно оси - будем считать, что угол 0

f1=input("Введите путь к файлу с координатами центра и радиуса элипса: ")
f2=input("Введите путь к файлу с координатами точек: ")




def pos_points(file1, file2):
    with open(f1,"r",encoding="utf-8",) as file1:
        x, y = [int(i) for i in file1.readline().rstrip().split()]  # координаты центра элипса
        r1, r2 = [int(i) for i in file1.readline().rstrip().split()]  # радиусы элипса

    with open(f2,"r",encoding="utf-8",) as file2:
        points = [
            [int(j) for j in i.split()] for i in [el.strip() for el in file2.readlines()]]  # список отчек
        positions = []
    for i in points:
        answer = (((i[0] - x) ** 2 / r1**2) + ((i[1] - y) ** 2 / r2**2) - 1)  # формула положения точки относительно элипса
        if answer == 0:
            positions.append(f"точка {tuple(i)} лежит на окружности")
        elif answer < 0:
            positions.append(f"точка {tuple(i)} внутри")
        else:
            positions.append(f"точка {tuple(i)} снаружи")

    return positions


print(*pos_points(f1, f2), sep="\n")
