def function_1():
     # collection: list
    # empty list
    # numbers_1 = list()
    numbers_1 = []
    print(f"numbers_1 = {numbers_1}, type = {type(numbers_1)}")

    numbers_2 = list()
    print(f"numbers_2 = {numbers_2}, type = {type(numbers_2)}")

function_1()


def function_2():
    # list of numbers
    numbers_1 = [10, 20, 30, 40, 50]
    print(f"numbers_1 = {numbers_1}")

    # list of numbers
    numbers_2 = list([10, 20, 30, 40, 50])
    print(f"numbers_2 = {numbers_2}")
function_2()


def function_4():
    # collection of mixed values
    mixed_values_1 = [10, 20, "india", True, False, "Usa", 40, 30.50]
    print(f"mixed_values_1 = {mixed_values_1}, type = {type(mixed_values_1)}")

    # collection of mixed values
    mixed_values_2 = list([10, 20, "india", True, False, "Usa", 40, 30.50])
    print(f"mixed_values_2 = {mixed_values_2}, type = {type(mixed_values_2)}")


function_4()
