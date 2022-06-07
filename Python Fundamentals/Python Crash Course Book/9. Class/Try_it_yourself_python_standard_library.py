# 9.13 OrderedDict Rewrite

from collections import OrderedDict

person = OrderedDict()
person = {
    'name': 'Hazrat_Mohammad(PBUH)',
    'Height': 'medium',
    'Color': 'Incomperable',
    'designation': 'Prophet',
    'city': 'Mecca',
    'age': 63,
}

for key, value in person.items():
    print(key + ' -> ' + str(value))

# 9.14 Dice

from random import randint

x = randint(1, 6)


class Dice:
    def __init__(self):
        self.sides = 6

    def roll_die(self, side):
        self.sides = randint(1, side)
        return self.sides


print("Printing results of 6 sided Dice")
for i in range(10):
    ludo = Dice().roll_die(6)
    print(ludo)

print("Printing results of 10 sided Dice")
for i in range(10):
    ludo = Dice().roll_die(10)
    print(ludo)

print("Printing results of 20 sided Dice")
for i in range(10):
    ludo = Dice().roll_die(20)
    print(ludo)
