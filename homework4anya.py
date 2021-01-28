################# 1

my_list = [-1, 1, 100, 200, 160, 400]
for value in my_list:
    if value > 100:
        print(value)

################# 2

my_list = [-1, 1, 100, 200, 160, 400]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)

################# 3

my_list = [-1, 1, 100, 200, 160, 400]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

################# 5

my_list = [6, 15, 1, -6, 0]
my_indexes = [0, 1, 2, 3, 4]
for index in my_indexes:
    print(my_list[index])

################# 6

my_list_1 = [6, 15, 1, -6]
my_list_2 = ["а", "о", "у", "э"]
my_indexes = [0, 1, 2, 3]
for index in my_indexes:
    print((my_list_1[index], my_list_2[index]))

################# 7

my_string = '0123456789'
my_list = []
for symbol_1 in my_string:
    for symbol_2 in my_string:
        my_list.append(int(symbol_1 + symbol_2))
print(my_list)