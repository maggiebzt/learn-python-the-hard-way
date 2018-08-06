# Create a class Parent
class Parent(object):
	
	# Method of class Parent which takes itself as a parameter
	def implicit(self):
		print "PARENT implicit()"

# Create a class Child which inherits Parent
class Child(Parent):
	pass

# Create a Parent object and call it dad
dad = Parent()

# Create a Child object and call it son
son = Child()

# Call on the method implicit
dad.implicit()
son.implicit()