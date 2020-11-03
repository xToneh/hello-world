#Antonio Perez
#November 3, 2020

#This program prints out if a number is divisible by three, five, or both.

number = int(input("Enter Number: "))
if (number % 3 == 0) and (number % 5 == 0) and (1 < number < 50):
    print("Number is divisible by both 3 and 5.")
elif (number % 3 == 0) and (1 < number < 50):
    print("Number is divisible by 3.")
elif (number % 5 == 0) and (1 < number < 50):
    print("Number is divisible by 5.")
else:
    print("Number is either not between 1 and 50 or not divisible by 3 or 5.")
