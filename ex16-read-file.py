from sys import argv

script, filename = argv

# Open file
target = open(filename, 'r')

target.close()