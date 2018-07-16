ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now" % len(stuff)

print "There we go: ", stuff # ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']

print "Let's do some things with stuff"

print stuff[1] # Oranges
print stuff[-1] # Corn
print stuff.pop() # Corn
print ' '.join(stuff) # Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
print '#'.join(stuff[3:5]) # Telephone#Light

#-------------------------
# Study Drills

# 1. ex: ' '.join(things)= join(' ', things)
# ten_things.split(' ')	 = split(' ', ten_things)
# more_stuff.pop()		 = pop(more_stuff)
# stuff.append(next_one) = append(next_one, stuff)
# stuff.pop()			 = pop(stuff)
# ' '.join(stuff)		 = join(' ', stuff)
# '#'.join(stuff)		 = join('#', stuff)