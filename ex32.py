the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i
	
#-------------------------
# Study Drill

# 2. avoid for loop
# initiate list
my_elements = []

# add ints to the list
my_elements = range(0, 6)

# check if elements are in list
for i in my_elements:
	print "Element in my elements is:", i
	
# 3.
# count: return number of occurrences of value
print "count(value):", my_elements.count(2) # 1

# extend: extend list by appending elements from the iterable
# print "extend(iterable):", my_elements.extend(6)
# TypeError: 'int' object is not iterable
# http://thomas-cokelaer.info/blog/2011/03/post-2/
my_elements.extend([6])
print "extend(iterable):", my_elements

# index: return first index of value
print "index(value, [start, [stop]]):", my_elements.index(1) # 1

# insert: insert object before index
my_elements.insert(0, -1)
print "insert(index, object):", my_elements

# pop: remove and return item at index (default last)
print "pop():", my_elements.pop() # 6
print "pop([index]):", my_elements.pop(0) # -1

# remove: remove first occurrence of value
my_elements.remove(0)
print "remove(value):", my_elements

# reverse: reverse *in place*
my_elements.reverse()
print "reverse():", my_elements

# sort: stable sort *in place*
my_elements.sort()
print "sort():", my_elements
