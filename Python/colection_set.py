def function_1():

    # set
    set_1 = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"set_1 = {set_1}, type = {type(set_1)}")


function_1()

def function_2():
    s1 = {10, 20, 30, 40}
    s2 = {30, 40, 50, 60}

    print(f"s1 = {s1}, s2 = {s2}")

    print("-" * 50)

    print(f"s1 intersection s2 = {s1.intersection(s2)}")
    print(f"s2 intersection s1 = {s2.intersection(s1)}")

    print("-" * 50)

    print(f"s1 union s2 = {s1.union(s2)}")
    print(f"s2 union s2 = {s2.union(s1)}")

    print("-" * 50)

    print(f"s1 difference s2 = {s1.difference(s2)}")
    print(f"s2 difference s1 = {s2.difference(s1)}")

    print("-" * 50)


function_2()


def function_7():
    number = 12

    # print positive symbol
    print("decimal number = {0:+}".format(number))

    # print negative symbol
    print("decimal number = {0:-}".format(number))

    # decimal
    print("decimal number = {0}".format(number))

    # decimal
    print("decimal number = {0:n}".format(number))

    # decimal
    print("decimal number = {0:d}".format(number))

    # binary
    print("binary number = {0:b}".format(number))

    # octal
    print("octal number = {0:o}".format(number))

    # lower hexadecimal
    print("hexadecimal number = {0:x}".format(number))

    # upper hexadecimal
    print("hexadecimal number = {0:X}".format(number))


function_7()