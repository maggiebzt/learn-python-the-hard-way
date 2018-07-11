from sys import argv

# 2a. 
# Script with fewer arguments

script = argv

print "Ma script:", script
#print "My fourth variable is:", fourth

# If I only have 1 argument, print out would be:
# Ma script: ['ex13a.py']

# If I only have 1 argument and I give it another value, print out would be:
# Ma script: ['ex13a.py', 'ay']
# ^Interesting, this can only be done for 1 argument

# If I have 2 arguments, I must give another value, 
# even though the value is never used