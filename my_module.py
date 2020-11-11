#Antonio Perez
#November 10, 2020
#
#Module 6: Lab Activity
#
#1st function - print 10 random integers between 25 and 35.
import random
from math import sqrt

print("Random integer from 25 - 35: ")
for i in range (0,10):
    print(random.randrange(25,35))

#2nd function - takes a list as a parameter and returns a random element from the list.
list = [1,2,3,4,5,6,7,8,9,0]
print("Random number from list 0 - 9: ")
print(random.choice(list))

#3rd function - function that returns a random off integer between 0 and 100.
odd = 2*(random.randint(0,100)//2)+1
print("Random odd integer between 0 - 100: ")
print(odd)

#4th function - function that calculates pythagorean theorem.
print("Pythagorean Theorem: ")
a = int(input("a: "))
b = int(input("b: "))

c = sqrt(a**2 + b**2)
print("c = ",c)
