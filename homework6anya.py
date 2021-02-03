###################### 1

my_list = ["abc", "100", "Hello", "my_str", "lesson", "Homework6"]
new_list = []
for index, symbol in enumerate(my_list):
    if index % 2:
        symbol = symbol[::-1]
    new_list.append(symbol)
print(new_list)

###################### 2

my_list = ["apple", "Almond", "orange", "pineapple", "apricot", "banana", "avocado"]
new_list = []
for symbol in my_list:
    if symbol[0] == "a":
        new_list.append(symbol)
print(new_list)

###################### 3

my_list = ["apple", "cherry", "orange", "pineapple", "apricot", "lemon"]
new_list = []
for symbol in my_list:
    if "a" in symbol:
        new_list.append(symbol)
print(new_list)

###################### 4

my_list = ["abc", "100", 100, "my_str", "lesson", 0, -6, "Homework6", 9999]
str_list = []
for symbol in my_list:
    if type(symbol) == str:
        str_list.append(symbol)
print(str_list)

###################### 5

my_str = "apple and lemon are fruits"
my_list = []
for symbol in my_str:
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)

###################### 6

my_str_1 = "apple and lemon"
my_str_2 = "cherry, apricot and orange"
my_list = []
common_symbol = set(my_str_1).intersection(set(my_str_2))
my_list.extend(common_symbol)
print(my_list)

###################### 7

str_1 = "plum and lemon"
str_2 = "cherry, apricot and peanut"
my_list = []
for symbol_1 in str_1:
    for symbol_2 in str_2:
        if symbol_1 == symbol_2 and str_1.count(symbol_1) == str_2.count(symbol_2) == 1:
            my_list.append(symbol_1)
print(my_list)

###################### 8

person = {"Last Name": "Musk",
          "Name": "Elon",
          "Age": 49,
          "Address": {"Country": "USA",
                      "City": "Los Angeles",
                      "Street": "Ocean Avenue"},
          "Job": {"Employment": "working",
                  "Position": "CEO"}}
print(person["Job"]["Position"])

###################### 9

cake_recipe = {"Составляющие":
                   {"Коржи": {"мука": "120 г",
                              "молоко": "30 мл",
                              "масло": "30 мл",
                              "яйцо": "3 шт"},
                    "Крем": {"сахар": "120 г",
                             "масло": "150 г",
                             "сметана": "300 г",
                             "ваниль": "1 ч.л."},
                    "Глазурь": {"какао": "50 г",
                                "сахар": "30 г",
                                "масло": "20 г"}}}
print(cake_recipe["Составляющие"]["Коржи"]["молоко"])