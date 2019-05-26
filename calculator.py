userInput = "";
print("select the arithmetic operation to perform");
print("1.Addition \n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Power");
print("type 'quit' to exit");
while userInput!='quit':
    userInput = input("operation:")
    if userInput == 'quit':
        break;
    firstNumber = int(input("first number:"))
    secondNumber = int(input("first number:"))
    if userInput == "1":
        print(firstNumber+secondNumber);
    elif userInput == "2":
        print(firstNumber - secondNumber);
    elif userInput == "3":
        print(firstNumber * secondNumber);
    elif userInput == "4":
        print(firstNumber / secondNumber);
    elif userInput == "5":
        print(firstNumber % secondNumber);
    elif userInput == "6":
        print(firstNumber ** secondNumber);
    else:
        print("invalid input, try again!!")
        break;




