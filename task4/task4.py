import argparse
import os

def check_path(x):
    if not os.path.isfile(x):
        raise ValueError(f'Файл {x} не найден')

def check_contents(x):
    try:
        with open(x, "r", encoding="utf-8") as f:
            lines = [i.strip() for i in f.readlines() if i.strip()]
            if not lines:
                raise ValueError(f'Файл {x} пустой')
            return [int(i) for i in lines]
    except ValueError:
        try:
            with open(x, "r", encoding="utf-8") as f:
                lines = f.read().strip()
                if not lines:
                    raise ValueError(f'Файл {x} пустой')
                return [int(i) for i in lines.split()]
        except ValueError as e:
            raise ValueError(f'Файл содержит нечисловые данные {e}')
    except Exception as e:
        raise ValueError(f'Ошибка чтения файла {e}')


def main():
    parser = argparse.ArgumentParser(description='Программа, выводит минимальное количество ходов, требуемых для приведения всех элементов массива к одному числу',epilog='Пример:\npython task4.py --file file.txt\npython task4.py (Интерактивный режим)',formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--file',help='Введите название файла с числами массива:\n')

    args = parser.parse_args()

    try: 
        if args.file:
            print(f'\nРежим командной строки\n')
            f = args.file
        else:
            print(f'\nИнтерактивный режим\n')
            f = input('Введите название файла с числами массива:\n') 

        check_path(f)
        massiv = check_contents(f)
        print(count_step(massiv))

    except ValueError as e:
        print(f'❌ Ошибка: {e}')
    except Exception as e:
        print(f'⚠️ Неизвестная ошибка: {e}')
        




def count_step(x):
    mediana = round(sum(x) / len(x), 0) # находим и округляем среднее арифмеитческое
    cnt = 0
    for el in x:
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



if __name__ == "__main__":
    main()