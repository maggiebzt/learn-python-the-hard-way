i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now:", numbers
	print "At the bottom i is %d" % i
	
print "The numbers:"

for num in numbers:
	print num
	
#-------------------------
# Study Drill

# 1. 
def print_while_loop(int):
	a = 0
	string = ""
	while a < int:
		string += "a is %d\n" % a
		numbers.append(a)
		a += 1
	return string

# 2.
print "int = 0\n", print_while_loop(0) 
# Print "None". I expected it to print just nothing
# https://stackoverflow.com/questions/28812851/why-is-this-printing-none-in-the-output
print "int = 1\n", print_while_loop(1)
print "int = 10\n", print_while_loop(10)

# 3.
def print_while_loop2(int, increment):
	a = 0
	string = ""
	while a < int:
		string += "a is %d\n" % a
		numbers.append(a)
		a += increment
	return string
	
print "int = 11, increment = 5\n", print_while_loop2(11, 5) # 0, 5, 10