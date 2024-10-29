result = []


def collatz_sequence(num):
    result.append(num)
    if num == 1:
        print(*result)
    elif num % 2 == 0:
        collatz_sequence(num // 2)
    else:
        collatz_sequence(3 * num + 1)


def print_backwards(syntax):
    a = list(syntax)
    a.reverse()
    print(*a, sep="")


def hammer_profit(cost, sold):
    num = len(sold)
    amount = sum(sold)
    return amount - cost * num


def format_names(name_list):
    name1 = name_list[0]
    if "," in name1:
        pass
    else:
        name1 = name1.split()
        name1_first = name1[0]
        name1_second = name1[1]
        name1 = name1_second + ", " + name1_first
        name_list[0] = name1

    name2 = name_list[1]
    if "," in name2:
        pass
    else:
        name2 = name2.split()
        name2_first = name2[0]
        name2_second = name2[1]
        name2 = name2_second + ", " + name2_first
        name_list[1] = name2

    name3 = name_list[2]
    if "," in name2:
        pass
    else:
        name3 = name3.split()
        name3_first = name3[0]
        name3_second = name3[1]
        name3 = name3_second + ", " + name3_first
        name_list[2] = name3

    name4 = name_list[3]
    if "," in name4:
        pass
    else:
        name4 = name4.split()
        name4_first = name4[0]
        name4_second = name4[1]
        name4 = name4_second + ", " + name4_first
        name_list[3] = name4

    return name_list
