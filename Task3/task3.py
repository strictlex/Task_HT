import json

values = input("Введите путь расположения  файла values.json:\n")
tests = input("Введите путь расположения файла tests.json:\n")

with open(values, "r", encoding="utf-8") as v1:
    val = json.load(v1)
with open(tests, "r", encoding="utf-8") as t1:
    test = json.load(t1)


# создаем словарь id:value
ids, vals = [], []
for el in val.values():
    for i in el:
        ids.append(i["id"])
        vals.append(i["value"])
ids_vals = {k: v for k, v in zip(ids, vals)}

# функция замены значения value 
def swap_value(x):
    if isinstance(x, list):
        for k in x:
            for i in k:
                if k["id"] in ids_vals.keys():
                    k["value"] = ids_vals[k["id"]]
                if isinstance(k, (list, dict)):
                    swap_value(k[i])


for lst in test.values():
    swap_value(lst)

# создаем словарь и присваиваем ключу значение словаря test
report = {"report": test["tests"]}
data_report = input("Введите путь расположение для файла report.json:\n")
print()

with open(data_report, "w", encoding="utf-8") as d_r:
    json.dump(report, d_r, indent=2, ensure_ascii=False, sort_keys=True)

print(f"Файл report.json создан в директории {data_report}")