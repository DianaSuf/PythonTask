# Поиск разницы между двумя JSON-файлами
import json


def get_difference(old_data: dict, new_data: dict, diffs: dict):
    for key in old_data.keys():
        if key in old_data and key in new_data:
            if type(old_data[key]) is dict and type(new_data[key]) is dict:
                get_difference(old_data[key], new_data[key], diffs)
            else:
                if key in diff_list and old_data[key] != new_data[key]:
                    diffs[key] = new_data[key]


with open('json_old.json', 'r', encoding="UTF-8") as file:
    data_old = json.load(file)

with open('json_new.json', 'r', encoding="UTF-8") as file:
    data_new = json.load(file)

result = {}
diff_list = ['services', 'staff', 'datetime']
get_difference(data_old, data_new, result)
print(result)

with open("result.json", "w", encoding="UTF-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)