from sys import exit

prompt = "> "

def gold_room():
	"""You win the game if you're not greedy, loses if you're greedy."""
	
	print "This room is full of gold. How much do you take?"
	
	next = raw_input(prompt)
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	"""Allows user to advance to the next room iff bear is moved from the door.
	Else, the user dies."""
	print "There's a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	print "1 = take honey"
	print "2 = taunt bear"
	print "3 = open door"
	bear_moved = False
	
	while True:
		next = raw_input(prompt)
		
		if next == "1":
			dead("The bear looks at you then slaps your face off")
		elif next == "2" and not bear_moved:
			print "The bear has moved from the door, you can go through"
			bear_moved = True
		elif next == "2" and bear_moved:
			dead("The bear is pissed and chew your leg off")
		elif next == "3" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"

def cthulhu_room():
	"""Doesn't allow user to advance to the gold room."""
	print "Here you see the great evil Cthulhu"
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head?"
	print "1 = flee"
	print "2 = eat your head"
	
	next = raw_input(prompt)
	
	if "1" == next:
		start()
	elif "2" == next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	"""Print out reason of death and exit the game"""
	print why, "Good job!"
	exit(0)
	
def start():
	"""Starts the game with 2 options."""
	print "You are in a dark room"
	print "There's a door to your right and left"
	print "Which one do you take?"
	print "1 = left"
	print "2 = right"
	
	next = raw_input(prompt)
	
	if next == "1":
		bear_room()
	elif next == "2":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")	

start()

#-------------------------
# Study Drill & Notes

# Difference between is and ==
# http://www.mysamplecode.com/2012/11/python-difference-between-is-and-equals.html

