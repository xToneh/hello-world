#This program will take a password from the user and print an appropriate message
#The 'in' keyword checks to see if a value exists somewhere in the given string.

greeting = input("Hello, possible pirate! What's the password?")
if greeting in ("Arrr!"):
	print("Greetings, hater of pirates!")
else:
        print("Go away, pirate.")

#The messages are flipped, the password 'Arrr!' should greet the user and anything else should "Go away".
