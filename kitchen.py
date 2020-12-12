import living_room
import main_character

def start(player):
    print("'You choose to check out the kitchen for more clues.'")
    input()
    print("'You know that only the chef of the house is able to access the kitchen since he is the only one with a key.'")
    input()
    choice = input("'What do you want to do?'\n\"A\" - Check the sink.\n\"B\" - Check the counter.\n\"C\" - Check the stove.\n\"D\" - Open drawers. \n\"E\" - Go to the Living Room.\n\"F\" - Make an accusation on who the murderer is.\n\"I\" - Check your clues.\n")

#Choices for the Kitchen.
    while choice != "E":
        if choice == 'A':
            print("'You check the sink, only to find a pile of dirty dishes but one long strand of brown hair.'")
            input()
            player.clues.append("Clue #1 - Long strand on brown hair.")
        elif choice == 'B':
            print("'You check the counter and see that there is a knife holder meant to hold 5 knives, but one is missing.'")
            player.clues.append("Clue #2 - Missing Knife")
            input()
        elif choice == 'C':
            print("'You check the stove but see nothing out of the ordinary.'")
            input()
        elif choice == 'D':
            print("'You open up some of the drawers and see many kitchen appliances neatly organized.'")
            input()
        elif choice == "I":
            print(player.clues)
        else:
            main_character.guess_who()
            print("'Who is the killer?'\n\"A\" - Alfred\n\"B\" - George\n\"C\" - Regina\n\"D\" - Rebecca")
        choice = input("'What do you want to do?'\n\"A\" - Check the sink.\n\"B\" - Check the counter.\n\"C\" - Check the stove.\n\"D\" - Open drawers. \n\"E\" - Go to the Living Room.\n\"F\" - Make an accusation on who the murderer is.\n\"I\" - Check your clues.\n")
    living_room.start(player)
