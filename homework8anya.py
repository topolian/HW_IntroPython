from random import randint, choice
import string

#### 1

names = ["billgates", "elonmusk", "zuckerberg", "johnson"]
domains = ["edu", "gov", "ua", "org"]


def create_email(name_list, domain_list):
    name = choice(name_list)
    numb = randint(100, 999)
    lower_case = string.ascii_lowercase
    random_str = "".join(choice(lower_case) for _ in range(randint(5, 7)))
    domain = choice(domain_list)
    return name + "." + str(numb) + "@" + random_str + "." + domain


print(create_email(names, domains))

#### 2


def create_str(min_limit, max_limit):
    lower_case = string.ascii_lowercase
    return "".join(choice(lower_case) for _ in range(randint(min_limit, max_limit)))


rand_str = create_str(110, 120)
print(rand_str)

#### 3


def add_signs_numb_upper(random_str):
    random_str = list(random_str)
    random_str[0] = random_str[0].upper()
    random_str.append(".")
    index = 0
    while index + 10 < len(random_str) - 1:
        step = randint(1, 10)
        random_str[index + step] = choice([" ", ", ", " " + str(randint(1, 200)) + " "])
        index = index + step + 1
    random_str = "".join(random_str)
    split_list = random_str.split()
    number_1 = 0
    while number_1 < randint(5, 10):
        goal_index_1 = randint(1, len(split_list) - 2)
        split_list[goal_index_1] = split_list[goal_index_1].capitalize()
        number_1 += 1
    return " ".join(split_list)


new_str = add_signs_numb_upper(rand_str)


def move_to_next_line(modified_str):
    modified_str = list(modified_str)
    number_2 = 0
    while number_2 < randint(10, 15):
        goal_index_2 = randint(1, len(modified_str) - 2)
        if modified_str[goal_index_2] == " " or modified_str[goal_index_2] == ", ":
            modified_str[goal_index_2] = "\n"
        number_2 += 1
    return "".join(modified_str)


print(move_to_next_line(new_str))
