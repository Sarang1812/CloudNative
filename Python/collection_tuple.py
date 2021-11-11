def function_3():
    # tuple may have duplicate values
    numbers = (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
    print(f"numbers = {numbers}, type = {type(numbers)}")

    print(f"10 value is present {numbers.count(10)} times")
    print(f"10 value is present on {numbers.index(10)}")
    print(f"10 value is present on {numbers.index(10, 1)}")

    # tuple of one item not possible
    tuple_1 = (10)
    print(f"tuple_1 = {tuple_1}, type = {type(tuple_1)}")


function_3()