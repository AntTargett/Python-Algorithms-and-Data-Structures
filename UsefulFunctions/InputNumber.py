def InputNumber():
    while True:
        try:
            number = int(input("Please input an integer: "))
            if number > 0:
                break
            else:
                print("Your number was less than zero, please try again")
                return InputNumber()

        except ValueError:
            print("Sorry, please try again inputting an integer")
        else:
            break
    return number
