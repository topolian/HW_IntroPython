################### 1

my_int = 100690413008
my_str = str(my_int)
result = my_str.count("0")
print(result)

################### 2

my_int = 10069130087000
my_str = str(my_int)
zero_num = len(my_str) - len(my_str.rstrip("0"))
print(zero_num)

################### 3a

my_list_1 = [3, "a", 9, -25, "s", 3.14]
my_list_2 = ["ab", 33, 0, 199, -7]
my_result = []
my_result.extend(my_list_1[::2])
my_result.extend(my_list_2[1::2])
print(my_result)

################### 3b

my_list_1 = [4, 9, -22, 0, -2.2]
my_list_2 = [30, -3.14, 0, 1, 198, -7]
my_result = []
for symbol_1 in my_list_1:
 if not symbol_1 %  2:
  my_result.append(symbol_1)
for symbol_2 in my_list_2:
 if symbol_2 % 2:
  my_result.append(symbol_2)
print(my_result)

################### 4

my_list = [4, 9, -22, 0, -2.2, "a"]
new_list = []
new_list.extend(my_list[1:])
new_list.append(my_list[0])
print(new_list)

################### 5

my_list = [4, 9, -22, 0, -2.2, "a"]
my_list.append(my_list.pop(0))
print(my_list)

################### 6

my_str = "30 января 2021 года в 18 часов"
my_split = my_str.split(" ")
# print(my_split)
numer_list = []
for symbol in my_split:
 if symbol.isdigit():
  numer_list.append(int(symbol))
print(sum(numer_list))

################### 7

my_str = "HelloPython"
my_str = list(my_str)
new_list = []
if len(my_str) % 2:
 my_str.append("_")
for index, symbol in enumerate(my_str):
  if not index % 2:
   new_list.append(my_str[index] + my_str[index + 1])

print(new_list)

################### 8

my_str = "Hi, Python"
l_limit = "i"
r_limit = "o"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.find(r_limit)]
print(sub_str)

################### 9

my_str = "Hello, Python"
l_limit = "e"
r_limit = "o"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(sub_str)

################### 10

my_list = [7, 10, 17, 6, 0, 3, 2, -2, -5]
new_list = []
for index, symbol in enumerate(my_list):
    if symbol in my_list[1:-1] and symbol > my_list[index - 1] + my_list[index + 1]:
        new_list.append(symbol)
# print(new_list)
print(len(new_list))