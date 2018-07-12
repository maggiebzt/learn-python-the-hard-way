print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

prompt = "> "
door = raw_input(prompt)

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input(prompt)
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input(prompt)
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!" 

elif door == "3":
	print "There are 3 doors in front of you with signs on them"
	print "1. Silky road"
	print "2. Long road"
	print "3. Rocky road"
	
	destination = raw_input(prompt)
	
	if destination == "1"
		print "Let's walk through the silky road together"
	elif destination == "2"
		print "This journey would take around 100 years"
	else:
		print "It'll be a bumpy ride but short"
	
else:	
	print "You stumble around and fall on a knife and die. Good job!"