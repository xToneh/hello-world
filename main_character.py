class main_character:
    name = ""
    clues = []
    
#If player decides to make an accusation it will return to this section.
def guess_who():
    accusation = input("'Who is the killer?'\n\"A\" - Alfred\n\"B\" - George\n\"C\" - Regina\n\"D\" - Rebecca\n")
    if accusation == "C":
        print("Congratulations! You solved the murder!")
        quit()
    else:
        print("Incorrect. Game Over.")
        quit()
