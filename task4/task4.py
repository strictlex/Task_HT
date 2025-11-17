file = input("Введите путь к расположению файла с массивом: ")

def count_step(f):
    with open(file, "r", encoding="utf-8") as f:
        lst = [int(i.strip()) for i in f.readlines()]

        mediana = round(sum(lst) / len(lst), 0) # находим и округляем среднее арифмеитческое
        cnt = 0
        for el in lst:
            while el != mediana:
                if el < mediana:
                    el += 1
                    cnt += 1
                elif el > mediana:
                    el -= 1
                    cnt += 1
                if cnt > 20:
                    return "20 ходов недостаточно для приведения всех элементов массива к одному числу»"

    return cnt

print(count_step(file))
