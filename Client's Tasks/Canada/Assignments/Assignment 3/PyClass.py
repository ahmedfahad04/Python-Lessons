print('Suppose you have a simply supported beam of 10 m. You can put a load of 15 kN at any point to calculate the moment for any point of interest.')
while True:
    try:
        load = float(input("Please enter point of load (in meter): "))
        while True:
            if int(load)>=0 and int(load)<=10:
                interest = float(input("Please enter point of interest (in meter): "))
                
                while True:
                    if int(interest) >= 0 and int(interest) <= 10:
                        z = load - interest
                        bending_moment= 15000*z

                        if z>0:
                            print(f"\t* Bending Moment: {bending_moment} N-m. \n\t* Direction: Clockwise.")
                        elif z<0:
                            print(f"\t* Bending Moment: {bending_moment} N-m. \n\t* Direction: Anticlockwise.")
                        else:
                            print("No moment is created here.")
                    else:
                        print("Please input a number between 0 to 10.")
                        continue
                    break
            else:
                print("Please input a number between 0 to 10.")
                continue
            break
    except:
        print("Invalid input!")
        continue
    break

input("Press ENTER to close the program.")

# User persona...
# hygen freak
# someone having dry and freezy hair
# someone with OCD
# zar oily hair


# types of artifical lights
# pros and cons 
# benifit of having these lights
# current saving lights
# light is benificial for specific plants
# in depth knowledge about knowledge


# students (exam time)
# employees
# elderly people
# parents
# travelers