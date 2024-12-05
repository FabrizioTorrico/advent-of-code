import re


def solution_1():
    with open("input.txt") as file:
        data = file.readline()

    values = re.findall(r"mul\([\d]*,[\d]*\)", data)
    total_sum = 0
    for value in values:
        x, y = value[4:-1].split(",")
        print(x, y)
        total_sum += int(x) * int(y)
    print(total_sum)


def solution_2():
    with open("input.txt") as file:
        data = file.readline()

    values = re.findall(r"(mul\([\d]*,[\d]*\)|do\(\)|don\'t\(\))", data)
    total_sum = 0
    do = True
    for value in values:
        if value == "don't()":
            do = False
            continue

        if value == "do()":
            do = True
            continue

        if not do:
            continue

        x, y = value[4:-1].split(",")
        total_sum += int(x) * int(y)
    print(total_sum)


solution_2()
