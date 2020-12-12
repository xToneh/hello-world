import living_room
import kitchen
import main_character

def start(player):
    print("Alright, Detective, this is the Dining Room where the crime was commited,")
    print("Here is some information on the each of the four suspects if you want to read it.")
    print("Or just look around and see if there is any useful evidence to make your verdict on who is the killer.")
    print("............")
    choice = input("'What do you want to do?'\n\"A\" - Read background information on Alfred.\n\"B\" - Read background information on George.\n\"C\" - Read background information on Regina. \n\"D\" - Read background information on Rebecca. \n\"E\" - Go to the kitchen. \n\"F\" - Accuse who the murderer is.\n")

#Choices for the Dining Room.
    while choice != "E":
        if choice == 'A':
            print("Alfred is the butler of mansion and one of the trustsed advisors of the one that was murdered.")
            input()
        elif choice == 'B':
            print("George is one of the guests that was invited to mansion, close friends with the owner, has been seen around with Rebecca.")
            input()
        elif choice == 'C':
            print("Regina is one of the guests that was invited to the mansion, she is close friends with the chef of the mansion.")
            input()
        elif choice == 'D':
            print("Rebecca is the maid of the mansion, usually keeps quiet but is close to George.")
            input()
        else:
            main_character.guess_who()
            print("'Who is the killer?'\n\"A\" - Alfred\n\"B\" - George\n\"C\" - Regina\n\"D\" - Rebecca")
        choice = input("'What do you want to do?'\n\"A\" - Read background information on Alfred.\n\"B\" - Read background information on George.\n\"C\" - Read background information on Regina. \n\"D\" - Read background information on Rebecca. \n\"E\" - Go to the kitchen. \n\"F\" - Accuse who the murderer is.\n")
#This only happens if you press E.
    kitchen.start(player)
        
