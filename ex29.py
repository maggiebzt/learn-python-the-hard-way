people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is not doomed"

if people > cats:
	print "Not many cats! The world is ..."

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry"
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs"
	
if people <= dogs:
	print "People are less than or equal to dogs"

if people == dogs:
	print "People are dogs lol"
	
#-------------------------
# Study Drill

# 1. It runs the code under it if the condition is met

# 2. For python to know to only run that code when the if condition is met

# 3. The code would be ran even when the if condition is not met

# 4. 
if not False:
	print True

# 5. If we change the name, there would be an error because a variable
# is undefined. If we change the value, it would be fine.