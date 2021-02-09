from random import randint

###################### 1

rnd_list = [randint(1, 100) for i in range(20)]
print(rnd_list)

###################### 2

triangle = {"A": (randint(-10, 10),
                 randint(-10, 10),
                 randint(-10, 10)),
            "B": (randint(-10, 10),
                 randint(-10, 10),
                 randint(-10, 10)),
            "C": (randint(-10, 10),
                 randint(-10, 10),
                 randint(-10, 10))}
print(triangle)

###################### 3

def my_print(my_str):
    return "***" + my_str + "***"
print(my_print("Hello, World!"))

###################### 4

persons = [{"name": "John", "age": 15},
           {"name": "Jessica", "age": 33},
           {"name": "Michael", "age": 45},
           {"name": "Jack", "age": 15},
           {"name": "Jane", "age": 27}]
# 4а
age_list = [dict["age"] for dict in persons]
age_set = set(age_list)
min_age = min(age_set)
for dict in persons:
    if min_age == dict["age"]:
        print(dict["name"])

# 4б
names = set(dict["name"] for dict in persons)
max_len = max(len(name) for name in names)
for dict in persons:
    if max_len == len(dict["name"]):
        print(dict["name"])

# 4в
average = sum(age_list) / len(age_list)
print(average)

###################### 5

my_dict_1 = {"01": "january",
             "04": "april",
             "06": "june",
             "09": "september"}
my_dict_2 = {"04": "апрель",
             "05": "may",
             "08": "august",
             "09": "сентябрь",
             "10": "october" }
# # 5a
common_key = set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))
common_key = list(common_key)
print(common_key)

# 5б
diff_key = set(my_dict_1.keys()).difference(set(my_dict_2.keys()))
diff_key = list(diff_key)
print(diff_key)

# 5в
my_dict_3 = {key:value for key, value in my_dict_1.items() if key in diff_key}
print(my_dict_3)

# 5г
dict_union = {**my_dict_1, **my_dict_2}
for key in dict_union.keys():
    if key in common_key:
        dict_union[key] = [my_dict_1[key], my_dict_2[key]]
print(dict_union)