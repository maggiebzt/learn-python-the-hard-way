from sys import argv

script, place_of_origin = argv

# Define the function where are you from
def where_are_you_from(country):
	return "I am from %s." % country
	
# Define the function how old are you
def how_old_are_you(age):
	return "I am %d years old." % age

origin = 'Indonesia'
current_age = 23

# Variable
print "1.", where_are_you_from(origin)

# 2 strings
print "2.", where_are_you_from('Jakarta, Indonesia')

# String and variable
print "3.", where_are_you_from('Jakarta, ' + origin)

# Itself as an argument and string
print "4.", where_are_you_from(where_are_you_from('Jakarta'))

# Another function
print "5.", where_are_you_from(how_old_are_you(current_age))

# String and another function
print "6.", where_are_you_from(('Jakarta. ' + how_old_are_you(current_age)))

# Variable and string from another function
print "7.", where_are_you_from(origin + how_old_are_you(current_age))

# Itself as an argument and variable
print "8.", where_are_you_from(where_are_you_from(origin))

# Use argv
print "9.", where_are_you_from(place_of_origin)

# Ask the user to input the data
print "10.", where_are_you_from(raw_input('> '))