import json

with open("jj.json") as tests:
    json_test = json.load(tests)
    print(json_test)
