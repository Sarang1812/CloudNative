def function_1():
    numbers = [10, 20, 30, 40, 50]
    # print(numbers)

    for value in numbers:
        print(f"value = {value}, type = {type(value)}")


function_1()


def function_2():
    countries = ["india", "usa", "japan"]

    for country in countries:
        print(f"country = {country}")


function_2()


def function_3():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # append a value at the end of the list
    numbers.append(60)
    print(numbers)

    numbers.append(70)
    print(numbers)

    # remove the last value
    popped_value = numbers.pop()
    print(f"remove the last value = {popped_value}")
    print(numbers)

    popped_value = numbers.pop()
    print(f"remove the last value = {popped_value}")
    print(numbers)

    popped_value = numbers.pop()
    print(f"remove the last value = {popped_value}")
    print(numbers)

    numbers.reverse()
    print("reverse numbers")
    print(numbers)


function_3()


def function_4():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # insert a value in-between
    numbers.insert(1, 15)
    print(numbers)

    # insert a value in-between
    numbers.insert(3, 25)
    print(numbers)

    # remove a value in between
    numbers.pop(3)
    print(numbers)

    numbers.pop(1)
    print(numbers)

    # remove by values
    numbers.remove(50)
    print(numbers)


function_4()


def function_5():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    print(f"count of values in numbers = {len(numbers)}")

    numbers.append(60)
    print(f"count of values in numbers = {len(numbers)}")

    numbers.pop()
    print(f"count of values in numbers = {len(numbers)}")


function_5()


def function_2():
    # list of int numbers
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # negative indexing
    print(f"numbers[0] = numbers[-5] = {numbers[-5]}")
    print(f"numbers[2] = numbers[-3] = {numbers[-3]}")
    print(f"numbers[4] = numbers[-1] = {numbers[-1]}")

    positions = range(len(numbers))
    print(positions)
    for index in positions:
        print(f"numbers[{-(index + 1)}] = {numbers[-(index + 1)]}")


function_2()


def function_3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # find all the values on even positions
    print(f"numbers[0:10:2] = {numbers[0:10:2]}")
    print(f"numbers[::2]    = {numbers[::2]}")

    # find all the values on odd positions
    print(f"numbers[1:10:2] = {numbers[1:10:2]}")
    print(f"numbers[1::2]    = {numbers[1::2]}")


function_3()