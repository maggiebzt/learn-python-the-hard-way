# Create a class called Parent
class Parent(object):

	# Method within the class parent
	def override(self):
		print "PARENT override()"

# Create a class called Child which inherits Parent
class Child(Parent):
	
	# Method within the class child
	# This method overrides the override method
	# inherited from the Parent class
	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
# This calls the override in the Child class
# instead of Parent class
son.override()