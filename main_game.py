import dining_room
import main_character as mc

player = mc.main_character()

#Intro
print("You walk into a crime scene with many cop cars in front of a mansion and a young looking cop begins to approach you.")
input()


player.name = input("Hello uhh, I'm sorry what was the name again detective? \n")
print("Hello Detective,",player.name)
input()
print("A big wealthy guy who owned this mansion was murdered after having a little get-together with some 'friends'.")
input()
print("We have four suspects here that could have possibly done it.")
input()
print("Think you can have a look around the crime scene and figure out which one of the four did it?")
input()

#Starting the next section of the game.
dining_room.start(player)
