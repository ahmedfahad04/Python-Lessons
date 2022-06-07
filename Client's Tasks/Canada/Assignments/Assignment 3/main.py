
def getPositiveNumber(promt):
    while True:

        n = input(promt).strip()

        if n != '':

            # this try catch handle the type error situation
            try:
                n = eval(n, {}, {})
            except:
                print("{} is not valid! Please enter Numbers: ".format(n))

            else:
                if type(n) is int or type(n) is float:
                    return n
                else:
                    print(n, " is not a number!")
        else:
            print("Missing Input!")


def myinput(promt):
    while True:

        n = input(promt).strip()

        if n != '' :
            try:
                if type(eval(n)) is int:
                    return n 
                else:
                    print(n, " is not a number!")
            except TypeError:
                print("String are not allowed. Please enter valid Numbers")

        else:
            print("Missing Input!")


getPositiveNumber("Enter number: ")