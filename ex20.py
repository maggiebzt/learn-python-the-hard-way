# Import argv variables from sys module
from sys import argv

# Define argv variables
script, input_file = argv

# Define print all function
def print_all(f):
	print f.read()

# Define rewind function
def rewind(f):
	f.seek(0)

# Define print a line function
def print_a_line(line_count, f):
	print line_count, f.readline()

# Open file inserted as an argv by the user
current_file = open(input_file)

print "First, let's print the whole file:\n"

# Print the whole current file
print_all(current_file)

print "Now, let's rewind"

# Rewind the current file's position 
rewind(current_file)

print "Let's print three lines:"

# Print the first line of current file
current_line = 1
print_a_line(current_line, current_file) # current_line = 1

# Print the second line of current file
current_line = current_line + 1
print_a_line(current_line, current_file) # current_line = 2

# Print the third line of current file
current_line = current_line + 1
print_a_line(current_line, current_file) # current_line = 3