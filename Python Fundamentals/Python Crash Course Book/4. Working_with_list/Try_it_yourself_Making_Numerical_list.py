#4.3 counting to twenty

for item in range(1,21):
    print(item,end=' ')

print(end='\n')
print("-------------------------------------")
#4.4 one million

# for item in range(1,1000001): # it will take too long time
#   print(item)

print("-------------------------------------")
#4.5 summing a million

summ=0
for item in range(1,1000001): # it is really too fast
    summ+=(item)

print(summ)

print("-------------------------------------")
#4.6 odd numbers

for item in range(1,20,2):
    print(item,end=' ')

print(end='\n')
print("-------------------------------------")
#4.6 threes

for item in range(3,31,3):
    print(item,end=' ')

print(end='\n')

print("-------------------------------------")
#4.7 cubes

for item in range(1,11):
    print(item**3, end=' ')

print(end='\n')
print("-------------------------------------")
#4.8 cubes comprehension

cube = [item**3 for item in range(1,11)]
print(cube, end=' ')


    
