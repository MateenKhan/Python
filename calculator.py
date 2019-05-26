def print_info():
    print("\n\ntype 'quit' to exit\n\n")
    print("select the arithmetic operation to perform")
    print("1.Addition \t2.Subtraction\t3.Multiplication\t4.Division\t5.Modulus\t6.Power")



def get_user_input():
    user_input = input("operation:");
    return user_input


def is_valid_user_input(user_input):
    try:
        user_selection = int(user_input)
        if user_selection < 1 or user_selection > 6:
            print("\n\nInvalid option selected try again!!")
            return False
    except ValueError:
        print("\n\nInvalid option selected try again!!")
        return False
    return True


def calculator(user_input):
    while user_input != 'quit':
        user_input = get_user_input()
        if user_input == 'quit':
            break
        if not is_valid_user_input(user_input):
            print_info()
            continue

        first_number = int(input("first number:"))
        second_number = int(input("first number:"))
        if user_input == "1":
            print(first_number+second_number)
        elif user_input == "2":
            print(first_number - second_number)
        elif user_input == "3":
            print(first_number * second_number)
        elif user_input == "4":
            print(first_number / second_number)
        elif user_input == "5":
            print(first_number % second_number)
        elif user_input == "6":
            print(first_number ** second_number)
        else:
            print("invalid input, try again!!")
            break


print_info()
calculator(user_input="")
