import argparse
import os

def check_path(f1,f2):
    for el in (f1,f2):
        if not os.path.isfile(el):
            raise ValueError(f' Файл {el} не найден!')
    
    return f1,f2

def interactive_input():
    f1 = input("Введите путь к файлу с координатами центра и радиуса элипса: ")
    f2 = input("Введите путь к файлу с координатами точек: ")
    return f1, f2


def main():
    parser = argparse.ArgumentParser(
        description="Программа расчитывает положение точек относительно окружности эллипса",
        epilog="Пример:\npython task2.py --file1 centr_rad.txt --file2 coord_points.txt\npython task2.py (Интерактивный режим)\nЕсли файлы находятся не в папке с текущей программой - нужно указать абсолютный путь к файлу",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--file1",help="Введите название файла с коориднатами центра эллипса и радиусами",)
    parser.add_argument("--file2", help="Введите название файла с коориднатами точек")

    args = parser.parse_args()

    try:
        if all([args.file1, args.file2]):
            print("\nРежим командной строки")
            f1, f2 = args.file1, args.file2

        else:
            print("\nИнтерактивный режим")
            f1, f2 = interactive_input()

        check_path(f1,f2)


        print(*pos_points(f1, f2), sep="\n")
    
    except ValueError as e:
        print(f"❌ Ошибка: {e}")
    except Exception as e:
        print(f"⚠️ Неизвестная ошибка: {e}")

def pos_points(f1, f2):
    with open(f1,"r",encoding="utf-8",) as file1:
        if  len([int(i) for i in file1.readline().rstrip().split()]) != 2:
            raise ValueError(f'В первой строке файла {f1}  - должно быть 2 числа')
        if  len([int(i) for i in file1.readline().rstrip().split()]) != 2:
            raise ValueError(f'Во второй строке файла  {f1}  - должно быть 2 числа радиуса')
        file1.seek(0)
        x, y = [int(i) for i in file1.readline().rstrip().split()]  # координаты центра элипса
        
        r1, r2 = [int(i) for i in file1.readline().rstrip().split()]  # радиусы элипса

    with open(f2,"r",encoding="utf-8",) as file2:
        for line in file2.readlines():
            if len([int(i) for i in line.rstrip().split()]) != 2:
                raise ValueError(f'В каждой строке файла {f2} должно быть по 2 числа')
        file2.seek(0)
        points = [[int(j) for j in i.split()]for i in [el.strip() for el in file2.readlines()]]  # список отчек
        positions = []
    for i in points:
        answer = (((i[0] - x) ** 2 / r1**2) + ((i[1] - y) ** 2 / r2**2) - 1 )  # формула положения точки относительно элипса
        if answer == 0:
            positions.append(0)
        elif answer < 0:
            positions.append(1)
        else:
            positions.append(2)

    return positions




if __name__ == "__main__":
    main()
