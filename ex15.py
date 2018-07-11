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
print "Type the filename again:"

# Save user response as a variable
file_again = raw_input('> ')

# Open the file and save it as a variable
txt_again = open(file_again)

# Read the file and print it out
print txt_again.read()

#------------------
# Study Drills
# 1. Written above

# 2. 
# open(): 
# 	takes 2 parameters: filename and mode
# 	there are 4 different modes:
#		"r": read   - default value. Error if file doesn't exist
#		"a": append - opens a file for appending. Create file if doesn't exist
#		"w": write  - opens a file for writing. Creates file if doesn't exist
#		"x": create - creates the specified file. Error if file exists
#	can specify if the file should be handled as binary or text mode:
#		"t": text   - default value, text mode
#		"b": binary - binary mode (e.g. images)\
#		e.g: f = open("demo.txt", "rt")
#	Source: https://www.w3schools.com/python/python_file_handling.asp
#
# file.read():
#	takes 1 parameter: number_of_characters
#		e.g. file = open("demo.txt")
#			 print file.read(5) -> output will only be the first 5 chars in demo.txt
#			 output example: Hello

# 3. I'm used to calling it functions.

# 4. ex15a.py

# 5. ex15b.py

# 6. ex15c.py

# 7.
# In terminal:
#	- run $ python
#	- >>> filename = 'ex15.py'
#	- >>> txt = open(filename) #open files
# 	- >>> print txt.read() #read files
# Not sure how to run a python file from within python, will skip this now

# 8.
txt.close()
txt_again.close()