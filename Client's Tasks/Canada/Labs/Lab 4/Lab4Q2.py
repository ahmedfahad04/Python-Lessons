# Lab4Q2.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        4 Question 2
# Author:     Wasif
# Version:    2021/02/19
# 
# Purpose:    The purpose of this question is to write a python program (script) to compute lists of
#             equally spaced time values and corresponding heights for a ball thrown straight up into the
#             air.
# 
# v0 = Initial velocity
# t0 = Difference of equally spaced time values
# interval = Number of interval
# cnt = Equally spaced time vlaues


from time import ctime

print("\n" + "-"*50 )

v0 = float(input("Enter the initial velocity in m/s: ")) 
interval = int(input("Enter the number of intervals: ")) 

t0 = (2*v0/9.81)/interval 
cnt = 0

time = []
for i in range(interval+1):
    time.append(float(cnt)) #adding the time values to "time" list
    cnt += t0 
    

height = []
for i in range(interval+1):
    eqn = v0*time[i] - 0.5*9.81*(time[i]**2) #core equation of finding height 
    height.append(eqn) #adding heights to "height" list
    
print("\ny(t) = v0*t - 0.5*g*t**2, where v0 is %.2f m/s\n" % v0)

print("\tt\t\t\t  y(t)")
for t,h in zip(time, height):
    print("%.7f" % t, "%14.7f"%h)



print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    