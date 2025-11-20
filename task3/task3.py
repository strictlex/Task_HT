import json
import argparse
import os

def check_path(f1,f2):
    for el in (f1,f2):
        if not os.path.isfile(el):
            raise ValueError(f'Файл {el} не найден!')
    return f1,f2

def valid_json_struct(data, struct, f):
    for key, value in struct.items():
        if key not in data:
            raise ValueError(f'Отсутствует обязательный ключ {key} в  {f}')
        elif  not isinstance(data[key], value):
            raise ValueError(f'Тип значения ключа {key} должен быть {value}')


def interactive_input():
    f1 = input('Введите название файла json который содержит результаты прохождения тестов с уникальными id:\n')
    f2 = input('Введите название файла json который содержит структуру для построения отчета на основе прошедших тестов:\n')
    f3 = input('Введите название файла json который будет заполнен полями value для структуры tests.json на основании values.json:\n')
    return f1,f2,f3


def main():
    parser=argparse.ArgumentParser(description='Программа формирует файл report.json с заполненными полями value для структуры tests.json на основании values.json', epilog= 'Пример:\npython task3.py --file1 values.json --file2 tests.json --file3 report.json\npython task3.py (Интерактивный режим)', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--file1', help='Введите название файла json который содержит результаты прохождения тестов с уникальными id:\n')
    parser.add_argument('--file2', help='Введите название файла json который содержит структуру для построения отчета на основе прошедших тестов:\n')
    parser.add_argument('--file3', help='Введите название файла json который будет заполнен полями value для структуры tests.json на основании values.json:\n')

    args=parser.parse_args()

    try:
        if all([args.file1,args.file2,args.file3]):
            #print(f'\nРежим командной строки')
            f1,f2,f3 = args.file1,args.file2,args.file3
        else:
            print(f'\nИнтерактивный режим')
            f1,f2,f3 = interactive_input()

        check_path(f1,f2)
        # valid_json(f1,f2)
        open_and_insert(f1,f2,f3)
        print(f'\nФайл {f3} выгружен')
    except ValueError as e:
        print(f'❌ Ошибка: {e}')
    except Exception as e:
        print(f'⚠️ Неизвестная ошибка: {e}')


def swap_value(x):
    if isinstance(x, list):
        for k in x:
            for i in k:
                if k["id"] in ids_vals.keys():
                    k["value"] = ids_vals[k["id"]]
                if isinstance(k, (list, dict)):
                    swap_value(k[i])

def open_and_insert(f1,f2,f3):
    try:
        with open(f1, "r", encoding="utf-8") as v1:
            val = json.load(v1)

        val_struct = {'values': list}
        valid_json_struct(val, val_struct,f1)

    except json.JSONDecodeError as e:
        raise ValueError(f'Файл {f1} содержит невалидный JSON: {e}')
    
    try:        
        with open(f2, "r", encoding="utf-8") as t1:
            test = json.load(t1)
        test_struct = {'tests': list}
        valid_json_struct(test, test_struct,f2)

    except json.JSONDecodeError as e:
        raise ValueError(f'Файл {f2} содержит невалидный JSON: {e}')



    # создаем словарь id:value
    ids, vals = [], []
    for el in val.values():
        for i in el:
            ids.append(i["id"])
            vals.append(i["value"])
    global ids_vals
    ids_vals = {k: v for k, v in zip(ids, vals)}

    


    for lst in test.values():
        swap_value(lst)

    # создаем словарь и присваиваем ключу значение словаря test
    report = {"report": test["tests"]}

    with open(f3, "w", encoding="utf-8") as d_r:
        json.dump(report, d_r, indent=2, ensure_ascii=False, sort_keys=True)

    return f3
    




if __name__ == '__main__':
    main()