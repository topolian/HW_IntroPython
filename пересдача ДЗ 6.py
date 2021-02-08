###################### 5

my_str = "apple and lemon are fruits"
my_list = []
my_set = set(my_str)
for symbol in my_set:
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)

###################### 7

str_1 = "plum and lemon"
str_2 = "cherry, apricot and peanut"
my_list = []
set_1 = set(str_1)
set_2 = set(str_2)
common_symb = set_1.intersection(set_2)
for symbol in common_symb:
        if str_1.count(symbol) == str_2.count(symbol) == 1:
            my_list.append(symbol)
print(my_list)