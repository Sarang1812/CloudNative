# empty function
def function_1():
    print("inside function 2")
    pass
# parameterless function definition
def function_2():
    print("inside function 2")
# parameterized function
def function_3(psrameterized_function):
    print("inside function 3")
    print(f"psrameterized_function={psrameterized_function},type={type(psrameterized_function)}")

# int
function_3(10)
print("==============================================================")
# float
function_3(15.50)
print("==============================================================")
# string
function_3("test")
print("==============================================================")
# bool
function_3(True)
print("==============================================================")

# function call
# function_2()
# print(function_2.__doc__)
# print(print.__doc__)
# print(type.__doc__)
print("==============================================================")
def can_vote(name,age):
    if age >=18:
        print(f"{name} is  eligible for voting")
    else:
        print(f"{name} is not eligible for voting")

can_vote("Sarang",18)
can_vote("surabh",10)
print("==============================================================")