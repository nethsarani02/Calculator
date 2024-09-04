def a():
    first_number = input("Type  here first number :")
    first_number = int(first_number)
    second_number = input("Type here second number :")
    second_number = int(second_number)
    answer = first_number + second_number
    print("The sum is:", answer)


def b():
    first_number = input("Type  here first number :")
    first_number = int(first_number)
    second_number = input("Type here second number :")
    second_number = int(second_number)
    answer = first_number - second_number
    print("The difference is:", answer)


def c():
    first_number = input("Type  here first number :")
    first_number = int(first_number)
    second_number = input("Type here second number :")
    second_number = int(second_number)
    answer = first_number * second_number
    print("The multiply is:", answer)


def d():
    first_number = input("Type  here first number :")
    first_number = int(first_number)
    second_number = input("Type here second number :")
    second_number = int(second_number)
    answer = first_number / second_number
    print("The quotient is:", answer)


def checking():
    user_input = input("Choose an operation (a: add, b: subtract, c: multiply, d: divide): ")
    if user_input == "a":
        a()
    elif user_input == "b":
        b()
    elif user_input == "c":
        c()
    elif user_input == "d":
        d()
    else:
        print("Invalid option")


print("Welcome SP calculator")
checking()