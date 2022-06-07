def getPositiveNumber(prompt):
    while True:

        n = input(prompt).strip()

        if n != '':
            try:
                n = eval(n, {}, {})
            except:
                print("{} is not valid!".format(n))

            else:
                if type(n) is int or type(n) is float:
                    if n >= 0:
                        break
                    else:
                        print(n, "is less than zero!")
                else:
                    print(n, " is not a number!")
        else:
            print("Missing Input!")

    return n

