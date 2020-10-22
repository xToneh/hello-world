#player_actions.py
#
#Antonio Perez
#October 20, 2020
#
#The two possible answers that the user can give.
yes = "Y"
no = "N"
#The program will start by asking player if he/she wants to play again
user_input = input("Would you like to play again? Type Y for Yes or N for No: \n")
#If the user types in "Y" then it will print out "Yes, play again."
if user_input == yes:
    print("Yes, play again.")
#If the user types in "N" then it will print out "No, do not play again."
elif user_input == no:
    print("No, do not play again.")
#If the user types anything else other than "Y" or "N" then it will print out "Invalid input."
    
else:
    print("Invalid input.")
    


