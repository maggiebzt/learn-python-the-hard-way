# Study drill #4

from sys import argv

# Argument variables
script, filename = argv

# Open the file and save it as a variable
txt = open(filename)

# Print out the filename
print "Here's your file %r:" % filename

# Read the file and print it out
print txt.read()

# Prompt user to input another file name
#print "Type the filename again:"

# Save user response as a variable
#file_again = raw_input('> ')

# Open the file and save it as a variable
#txt_again = open(file_again)

txt.close()