## Animal is-a object
class Animal(object):
	
	def jump(self):
		self.jump = True

## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		# Take attribute name from object self
		# and set it to name
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Take attribute name from object self
		## and set it to name
		self.name = name

## Person is-a object
class Person(object):

	def __init(self, name):
		## Take attribute name from self
		## and set it to name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
	def eat(food):
		## Take attribute last_meal from self
		## and set it to food
		self.last_meal = food
		
		## Take attribute full from self
		## and set it to true
		self.full = True

## Employee is-a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		# From super(Employee, self) get the 
		# __init__ function, and call it with
		# parameters self, name
		super(Employee, self).__init__(name)
		
		# Take salary attribute from self object
		# and set it to salary
		self.salary = salary
		
# Fish is-a object
class Fish(object):
	
	def __init__(self, name):
		self.name = name
	
# Salmon is-a Fish
class Salmon(Fish):
	pass
	
# Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet, and set its value to satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet, and set its value to rover
frank.pet = rover

## Set flipper to an instance of Fish
flipper = Fish()

## Set crouse to an instance of Salmon
crouse = Salmon()

## Set harry to an instance of Halibut
harry = Halibut()

#-------------------------
# Study Drill

# 2. No. We need to create an object that's an instance 
# of a class to use it.