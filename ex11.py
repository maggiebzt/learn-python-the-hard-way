print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input('--> ')

print "So, you're %r years old, %r tall, and %r heavy." % (
	age, height, weight)
	
#-------------------------
# Study Drill

# 1. raw_input() : prompt user to provide an input for the program
# and return the data input by the user in a string

# 3.
print "What's your first name?"
first_name = raw_input()

print "What's your last name?"
last_name = raw_input()

print "What's your middle name?"
middle_name = raw_input()

# 4. because it's displayed using %r. If we run this instead it won't 
# have that \'

print "So, you're %r years old, %s tall, and %r heavy." % (
	age, height, weight)