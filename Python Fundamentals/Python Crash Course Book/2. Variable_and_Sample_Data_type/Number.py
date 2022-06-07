a = 10
b = 4

print("Addition: %d" % (a+a))
print("Substraction: %d" % (a-b))
print("Multiplication: %d" % (a*b))
print("Power of b: %d" % (a**b))
#Division
print(a/b) #show with precision
print(a//b) #show just decimal portion
print("Division: %d"%(a/b)) #fomate modifier matters
print("Division: %f"%(a/b)) #fomate modifier matters

#msg = "His age is " + a + " years old" #make wrong output

msg = "His age is " + str(a) + " years old" 
#its correct. Changing type of variable like this is called type casting

print(msg)