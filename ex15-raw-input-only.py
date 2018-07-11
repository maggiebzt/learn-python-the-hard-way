from sys import argv

# Argument variables
script = argv

# Prompt user to insert filename
filename = raw_input("What's your file name?")

# Open the file and save it as a variable
txt = open(filename)

# Print out the filename
print "Here's your file %r:" % filename

# Read the file and print it out
print txt.read()

# Prompt user to input another file name
print "Type the filename again:"

# Save user response as a variable
file_again = raw_input('> ')

# Open the file and save it as a variable
txt_again = open(file_again)

# Getting the filename using argv is better because the user can use 'ls'
# to check existing files or TAB to complete the file name (IFF it exists).
# Whereas with raw_input(), the user needs to type in every single character
# themselves. Using argv ensures the file exists ('ls') or there's no typo (TAB)

txt.close()
txt_again.close()