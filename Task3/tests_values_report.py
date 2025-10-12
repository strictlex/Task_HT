import json
# создаем переменные из считынных файлов json
file_t = "/Users/aleksey/Documents/python/Tasks_HT/Task3/tests.json"
file_v = "/Users/aleksey/Documents/python/Tasks_HT/Task3/values (1).json"
with open(file_t, "r", encoding="utf-8") as tests:
    data_tests = json.load(tests)
with open(file_v, "r", encoding="utf-8") as values:
    data_values = json.load(values)

# словарь  id: value
ids = []
vals = []
for lst in data_values["values"]:
    ids.append(lst["id"])
    vals.append(lst["value"])
ids_vals = {k: v for k, v in zip(ids, vals)}  

# реркурсивная
def swap_value(x):
    if isinstance(x, list):
        for k in x:
            for i in k:
                if k["id"] in ids_vals.keys():
                    k["value"] = ids_vals[k["id"]]
                if isinstance(x, (list,dict)):
                    swap_value(k[i])


# поиск по id в переменной data_tests
for lst in data_tests.values():
    swap_value(lst)


data_report = {"report": data_tests["tests"]}


with open("/Users/aleksey/Documents/python/Tasks_HT/Task3/report.json", "w", encoding="utf-8") as report:
    json.dump(
        data_report,
        report,
        ensure_ascii=False,
        indent=2,
        separators=(",", ":"),
        sort_keys=True,
        default=str,
    )
