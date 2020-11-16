#Antonio Perez
#November 17, 2020
#
#Write a program that takes a user input, then uses a while loop to check if that input is the letter A, B, or C. The loop should continue until a valid input is entered by the user

while True:
    x = input("Input the letter A, B, or C: ")
    if x != "A" or "a" and x != "B" and x != "C":
        print("Sorry, try again.")
    else:
        break

    
