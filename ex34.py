#-------------------------
# Study Drill

# 1.
# Cardinal numbers are for counting, ordinal numbers are for orders
# Cardinal example: 0 apples, 5 bottles -> can use 0
# Ordinal example: 1st kid, 3rd kid -> can't use 0, there's no 0th something
# https://www.quora.com/What-is-the-difference-between-ordinal-numbers-and-cardinal-numbers

# 2.
# The year 2010 is an ordinal number.

# 3. 
# Print out the object in list located at index
def cardinal_number(list, index):
	return "The object at %d is %r" % (index, list[index])

# Print out the index-th object in list
def ordinal_number(list, index):
	return "The %i-th object is %r" % (index, list[index - 1])
	
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "1.", cardinal_number(animals, 1)
print "2.", ordinal_number(animals, 3)
print "3.", ordinal_number(animals, 1)
print "4.", cardinal_number(animals, 3)
print "5.", ordinal_number(animals, 5)
print "6.", cardinal_number(animals, 2)
print "7.", ordinal_number(animals, 6)
print "8.", cardinal_number(animals, 4)
