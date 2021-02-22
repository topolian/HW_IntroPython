import json
from random import randint, uniform, choice, choices
import string

#### 1

with open("names.txt", "r") as txt_file:
    last_names = []
    for line in txt_file.readlines():
        last_names.append(line.split()[1])
print(last_names)

#### 2


def create_dict_js(numb_of_keys):
    rand_key_list = []
    numb = 0
    while numb < numb_of_keys:
        rand_key = "".join(choice(string.ascii_lowercase) for _ in range(5))
        rand_key_list.append(rand_key)
        numb += 1
    data = {rand_key: choices(["int_value", "float_value", "bool_value"])[0] for rand_key in rand_key_list}
    # choices без весов делает выбор с одинаковой вероятностью по документации
    for rand_key in data:
        if data[rand_key] == "int_value":
            data[rand_key] = randint(-100, 100)
        elif data[rand_key] == "float_value":
            data[rand_key] = uniform(0, 1)
        else:
            data[rand_key] = choice([True, False])
    return data


print(create_dict_js(randint(5, 20)))

#### 3

result = create_dict_js(randint(5, 20))


def generate_and_write_json(file_path):
    with open(file_path, "w") as js_file:
        json.dump(result, js_file, indent=2)


generate_and_write_json("3rd_task.json")
