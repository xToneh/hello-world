import main_character

def start(player):
    print("'You choose to check out the living room for more clues.'")
    input()
    print("'You see a couple things around the living room that might be important.'")
    input()
    choice = input("'What do you want to do?'\n\"A\" - Check under couch.\n\"B\" - Read letter on table.\n\"C\" - Dust for fingerprints. \n\"D\" - Accuse who the murderer is.\n\"I\" - Check your clues.\n")

#Choices for the Living Room.
    while choice != 'D':
        if choice == 'A':
            print("'You check under couch and find nothing but dust.'")
            input()
        elif choice == 'B':
            print("'You pick up the letter on the table that reads' \n""Dear friends, I welcome you to come and visit me this Friday coming up to have dinner at my house, I would love to make up for the way we settled things back a few months ago before we all went our seperate ways, if you decide to vist my butler Alfred will meet you at the gate to escort you in. See you then!")
            input()
            player.clues.append("Clue #3 - Invitation letter")
        elif choice == 'C':
            print("'You dust for finger prints and find that you see only George and Rebecca's fingerprints.'")
            input()
            player.clues.append("Clue #4 - George and Rebecca were together in the Living Room")
        elif choice == 'I':
            print(player.clues)
        else:
            print("'Who is the killer?'\n\"A\" - Alfred\n\"B\" - George\n\"C\" - Regina\n\"D\" - Rebecca")
        choice = input("'What do you want to do?'\n\"A\" - Check under couch.\n\"B\" - Read letter on table.\n\"C\" - Dust for fingerprints. \n\"D\" - Accuse who the murderer is.\n\"I\" - Check your clues.\n")
    main_character.guess_who()
