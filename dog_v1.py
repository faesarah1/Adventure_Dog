from sys import exit
from time import sleep
import os
import platform

really_bored = 0

def check_input():
	user_choice = input("> ")

	if user_choice.lower() == "q":
		print("Thanks for playing!")
		exit(0)
	elif user_choice.lower() == "r":
		restart()
	return user_choice

def adventure():
	print("\nYou are a dog.")
	print("You are an adventurous dog.")
	print("You are an adventurous dog who likes to make decisions.")
	print("Your first decision is whether to play outside or inside today.")
	print("[1] Outside sounds nice \n[2] Inside is cool")

	number_of_tries = 0
	while True:
		choice = check_input()

		if choice == "1" or "outside" in choice:
			change_room(door, 0)
		elif choice == "2" or "inside" in choice:
			change_room(inside, 0)
		else:
			if number_of_tries == 0:
				print("\nC'mon, man... we ain't got all day here. Make a decision!")
				number_of_tries += 1
			elif number_of_tries == 1:
				print("\nDude, seriously. I'm starting to get mad.")
				number_of_tries += 1
			else:
				dead("\nThat's it, I'm kicking you out of the game.")

def door():
	print("\nYou really want to go outside but the door is shut. What's your strategy?")
	print("[1] Scratch at the door \n[2] Bark at the door \n[3] Pee on the floor \n[4] You change your mind, inside sounds more interesting.")

	choice = check_input()

	if choice == "1" or "scratch" in choice:
		print("\nYou scratch furiously at the door, letting out an occasional whine. \nYour human comes and scolds you, then opens the door.")
		print("Finally, out of the house and into the sunshine!")
		change_room(front_yard, 8.0)
	elif choice == "2" or "bark" in choice:
		print("\nYou let out a mighty bark: Bark! \nbark, bark, bark, bark \nYour human comes and opens the door.")
		print("Finally, a taste of freedom!")
		change_room(front_yard, 8.0)
	elif choice == "3" or "pee" in choice:
		print("\nYou pee on the floor, right in a corner where it will be hard to clean.")
		dead("You get a swat on the nose and your human puts you in the kennel for the rest of the day.")
	elif choice == "4" or "inside" in choice or "change" in choice:
		change_room(inside, 0)
	else:
		print("\nClearly you don't have a cohesive plan so you sit and look longingly at the door for a while.")
		boredom()
		change_room(inside, 0)

def inside():
	
	while True:
		print("\nYou decide to the explore the house.")
		print("There is a lovely scent wafting from the kitchen.")
		print("Your food bowl is in the laundry room.")
		print("There are some tasty leather shoes in the closet upstairs to chew on.")
		print("[1] What's going on in the kitchen? \n[2] Go to the laundry room to get some grub \n[3] Shoes! \n[4] You change your mind, outside sounds better")
		
		choice = check_input()

		if choice == "1" or "kitchen" in choice:
			print("\nWhatever is going on in the kitchen seems interesting. You head that way to investigate.")
			change_room(kitchen)
			break
		elif choice == "2" or "laundry" in choice or "food" in choice:
			print("\nYour tummy rumbles and the laundry room seems like the clear choice. You head that way to get some vittles.")
			change_room(laundry)
			break
		elif choice == "3" or "shoes" in choice or "upstairs" in choice:
			print("\nYou've been eyeing a particularly juicy-looking pair of loafers. You head upstairs to find them.")
			change_room(upstairs)
			break
		elif choice == "4" or "outside" in choice or "change" in choice:
			change_room(door, 0)
			break
		else:
			print("\nClearly you don't have a cohesive plan so you sit and look longingly around the room.")
			back_to_prompt(5.0)

def front_yard():
	print("\nYou decide to explore the yard.")
	print("In the corner of the yard, you see a nice hole you've been working on.")
	print("The neighbor's dog is sitting by the fence.")
	print("The kids are blowing bubbles in the yard.")
	print("[1] Work on the hole \n[2] Head to the fence for some quality socialization \n[3] Bubbles! \n[4] Screw the yard... I want REAL freedom!")

	choice = check_input()

	if choice == "1" or "hole" in choice:
		print("\nThe fat, juicy bone isn't going to bury itself. Time to get some work done.")
		print("You head to the partially-dug hole and begin to add to your previous work.")
		print("Uh oh, your human is coming toward you and he doesn't look happy.")
		dead("You get a swat on the nose and your human puts you in the kennel for the rest of the day.")
	elif choice == "2" or "fence" in choice or "socialization" in choice or "dog" in choice:
		print("\nThe neighbor's dog is pretty cute and definitely worth some attention. You strut over in your most confident gait.")
		print("When you get to the fence, you smell something funny.")
		print("Something very peculiar that you don't like a t  a l l.")
		print("Is that..... the scent of another dog??")
		dead("Turns out your neighbor's dog already has a partner.")
	elif choice == "3" or "bubbles" in choice:
		print("\nCatching bubbles is the best activity in the world! \nYou run over to the kids and beginning snapping at bubbles.")
		dead("You lose track of time and spend the rest of the day playing with bubbles.")
	elif choice == "4" or "freedom" in choice:
		dead("\nYou run out of the yard and immediately get hit by a passing car.")
	else:
		print("\nClearly there are too many great options so you sit around and look longingly at the yard.")
		boredom()
		change_room(front_yard, 0)

def kitchen():
	
	while True:
		print("\nUpon arriving to the kitchen, you realize the amazing scent is coming from the counter.")
		print("You can't tell what it is, but your senses say that it is food. \nPeople food.\nThe best kind of food.")
		print("What's the plan here?")
		print("[1] Jump up and pull the food down \n[2] Stay away... trying to eat people food always leads to trouble.")

		choice = check_input()

		if choice == "1" or "jump" in choice:
			print("\nYou attempt to jump up and get the food.")
			print("You fall backwards and crash into the table, which gets the attention of your human.")
			dead("You get a swat on the nose and your human puts you in the kennel for the rest of the day.")
		elif choice == "2" or "stay" in choice:
			print("\nWise decision. You should probably find something else to do.")
			change_room(inside)
		else:
			print("\nThat's not an option.")
			back_to_prompt()
			
def laundry():
	print("\nYou stroll to the laundry room, the best room in the house.")
	print("In here you see your comfy bed, food bowl, and several toys.")
	print("[1] Take a nap \n[2] Eat some food \n[3] Play with a toy")

	while True:
		choice = check_input()

		if choice == "1" or "nap" in choice:
			print("\nYawn. A nap sounds great right now.")
			dead("You sleep for the rest of the day.")
		elif choice == "2" or "eat" in choice:
			print("\nWell sure, that's what we came in here for in the first place.")
			print("Nom nom nom")
			print("Now what?")
			boredom()
			change_room(inside, 0)
		elif choice == "3" or "toy" in choice:
			print("\nYou pick up the nearest chew toy in your mouth.")
			print("This seems nice... rubbery yet firm. Quality toys are a rare commodity these days.")
			print("Chew chew chew")
			print("Now what?")
			boredom()
			change_room(inside, 0)
		else:
			print("I don't know what that means.")
			back_to_prompt()
			
def upstairs():
	print("\nYou head upstairs to find those loafers you wanted to try.")
	print("At the top of the stairs, you have some options.")
	print("[1] Go to the left \n[2] Go to the right")

	while True:
		choice = check_input()

		if choice == "1" or "left" in choice:
			print("\nYou can't remember which closet you saw those loafers in but you think it might be this way.")
			print("You get to the bedroom but the door is tightly closed.")
			print("You turn around and walk to the other end of the hall.")
			change_room(bedroom, 10.0)
		elif choice == "2" or "right" in choice:
			print("\nYou can't remember which closet those loafers were in but this way seems like a good place to start.")
			change_room(bedroom)
		else:
			print("\nYou only have two options. Pick one.")
			back_to_prompt()
			
def bedroom():
	print("\nYou push the bedroom door open with your nose and make your way to the closet across the room.")
	print("You begin to dig around for those loafers.")
	print("Suddenly you are struck by a pang of guilt and wonder if you should continue.")
	print("[1] Nah, just ignore the guilt. These shoes are worth it. \n[2] On second thought, this might be a bad idea. Eating shoes always leads to trouble.")

	while True:
		choice = check_input()

		if choice == "1" or "ignore" in choice:
			print("\nYou find the shoes and begin to naw away.")
			print("Boy, were these worth it... so tasty.")
			print("Uh oh, your human is at the closet door!")
			dead("You get a swat on the nose and your human puts you in the kennel for the rest of the day.")
		elif choice == "2":
			print("\nWise decision. Humans really seem to like their shoes a lot.")
			print("You should probably find something else to do.")
			change_room(inside)
		else:
			print("\nWhat?")
			back_to_prompt(2.0)
			
def boredom():
	global really_bored
	if really_bored == 0:
		really_bored += 1
		sleep(2.0)
		print("\nBoredom sets in and you forget what you were doing here in the first place.")
		print("You look around, searching for a hint.\n")
		sleep(5.25)
		print("You scratch behind your ear. That feels pretty good.")
		print("You're getting distracted... focus!")
		sleep(4.25)
		print("\n\n")
		print("Nope. Nothing.")
		sleep(3.25)
		print("\n\n")
		input("Press [enter] to continue......")
	elif really_bored == 1:
		really_bored += 1
		sleep(2.0)
		print("\nBored again, you look for something to do.")
		print("You look around, wondering if you'll see something interesting.\n")
		sleep(4.75)
		print("You lick your balls. Nice.")
		print("Wait, you were looking for something, right?")
		sleep(3.75)
		print("\n\n")
		print("Hmmm if only you could remember...")
		sleep(2.75)
		print("\n\n")
		input("Press [enter] to continue......")
	elif really_bored == 2:
		really_bored = 0
		sleep(2.0)
		print("\nMan, being a dog can really get boring quite often.")
		print("Surely there's gotta be something interesting to do.\n")
		sleep(4.0)
		print("You sniff around for something... anything...")
		print("Hang on, what were you doing again?")
		sleep(3.0)
		print("\n\n")
		print("Nothing comes to mind")
		sleep(2.0)
		print("\n\n")
		input("Press [enter] to continue......")
	else:
		sleep(1.0)
		dead("There's only so many times you can handle being bored... time for a nap. \n")

def clear_screen():

	system = platform.system()

	if system == "Linux" or system == "Darwin":
		os.system("clear")
	elif system == "Windows":
		os.system("cls")

	print("\n   		   ***** Adventure Dog *****\n")
	print("Enter [Q] at any prompt to leave the game or [R] to restart the game.\n")		

def change_room(room, amt = 6.0):
	sleep(amt)
	clear_screen()
	room()

def dead(msg):
	print(msg, "RIP")
	print("\n\nPlay again? Y/N")

	choice = check_input()

	if choice.lower() == "y":
		return restart()
	elif choice.lower() == "n":
		exit(0)
	else:
		print("Y or N are the only options")

def back_to_prompt(amt = 3.0):
	sleep(amt)
	clear_screen()

def restart():
	# reset any persistent game state 
	clear_screen()
	print("\nIn case you forgot...")
	adventure()
	exit(0)

def start():
	clear_screen()
	adventure()

start()



