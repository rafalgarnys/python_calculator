def main():
    while 1:

        number_one = float(input("Type first number: "))
        operator_type = input("Operator type: ")
        number_two = float(input("Type second number: "))

        if operator_type == "+":
            result = number_one + number_two
        elif operator_type == "-":
            result = number_one - number_two
        elif operator_type == "*":
            result = number_one * number_two
        elif operator_type == "/":
            result = number_one / number_two
        else:
            result = number_one % number_two

        print("Your result: " + str(result))

        continuation = "x"
        while continuation != "y" and continuation != "n":

            print("Do you want to continue? Type Y/N")
            continuation = input().lower()
        if continuation == "n":
            break

if __name__ == "__main__":
    main()
