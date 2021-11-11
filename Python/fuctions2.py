# non-returning function
def add_1(n1, n2):

    print(f"{n1} + {n2} = {n1 + n2}")

answer_1 = add_1(10, 20)

print(f"answer_1 = {answer_1}")


# returning function
def add_2(n1, n2):

    return n1 + n2

answer_2 = add_1(20, 50)
print(f"answer_2 = {answer_2}")

answer_3 = add_2(10, 20)
print(f"answer_3 = {answer_3}")


def math_operations(n1, n2):
    addition = n1 + n2
    multiplication = n1 * n2
    division = n1 / n2
    subtraction = n1 - n2

    # return (addition, multiplication, division, subtraction)
    return addition, multiplication, division, subtraction


# answers = math_operations(20, 10)
# print(f"operation answers = {answers}")

addition, multiplication, division, subtraction = math_operations(20, 10)
print(f"addition = {addition}")
print(f"multiplication = {multiplication}")
print(f"division = {division}")
print(f"subtraction = {subtraction}")
