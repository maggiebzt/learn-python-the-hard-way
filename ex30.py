# Define variables
people = 30
cars = 40
buses = 15

# Print out when there's more car than people
if cars > people:
	print "We should take the cars."
# Print out when there's more people than car
elif cars < people:
	print "We should not take the cars."
# Print out when there's equal people and car
else:
	print "We can't decide."

# Print out when there's more buses than cars
if buses > cars:
	print "That's too many buses."
# Print out when there's more cars than buses
elif buses < cars:
	print "Maybe we could take the buses."
# Print out when there's equal buses and cars
else:
	print "We still can't decide."

# Print out when there's more people than buses
if people > buses:
	print "Alright, let's just take the buses."
# Print out when there's not more people than buses
else:
	print "Fine, let's stay home then"