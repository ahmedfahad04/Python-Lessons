#5.3 alien color 1

alien_colors = ['green','yellow','red']

if 'green' in alien_colors:
    print("+5 points")
else: 
    print("Missed it!")

if 'brown' in alien_colors:
    print("+5 points")
else:
    print("Missed it!")


print("------------------------------------------")
#5.4 alien color 2

if 'green' in alien_colors:
    print("Bingo!! +5 points added")
else:
    print("+10 points")


if 'brown' in alien_colors:
    print("Bingo!! +5 points added")
else:
    print("+10 points")

print("------------------------------------------")
#5.5 alien color 3

if 'green' in alien_colors:
    print("+5 points")
elif 'yellow' in alien_colors:
    print("+10 points")
elif 'red' in alien_colors:
    print("+15 points")
else:
    print("sorry bro!!")


if 'red' in alien_colors:
    print("+15 points")
elif 'yellow' in alien_colors:
    print("+10 points")
elif 'green' in alien_colors:
    print("+5 points")
else:
    print("sorry bro!!")

    
if 'yellow' in alien_colors:
    print("+10 points")
elif 'green' in alien_colors:
    print("+5 points")
elif 'red' in alien_colors:
    print("+15 points")
else:
    print("sorry bro!!")


print("------------------------------------------")
#5.6 stages of life

age = 7

if age<2:
    print("Baby")
elif age>=2 and age<4:
    print("toddler")
elif age>=4 and age<13:
    print("Kid")
elif age>=13 and age<20:
    print("Teenager")
elif age>=20 and age<65:
    print("Adult")
else:
    print("Elder")

print("------------------------------------------")
#5.7 favorite fruit

fruit = ['mango','jackfruit','banana','orange']

if 'mango' in fruit:
    print("Its my favorite fruit")
elif 'jackfruit' in fruit:
    print("This the national fruit of Bangladesh")
elif 'banana' in fruit:
    print("Its full of pottasium")
else:
    print("AH!!")
# type 3 types of elif statements like the 5.5 exercise