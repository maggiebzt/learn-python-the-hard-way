# stuff {'name': 'Zed', 'age': 36, 'height': 74}

# Create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print '-' * 10
print 'NY state has: ', cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

#-------------------------
# Study Drill

# 1.
kalimantan_capital_cities = {
	'West Kalimantan' : 'Pontianak',
	'South Kalimantan' : 'Banjarmasin',
	'Central Kalimantan' : 'Palangkaraya',
	'East Kalimantan' : 'Samarinda',
	'North Kalimantan' : 'Tanjungselor'
}

java_capital_cities = {
	'Banten' : 'Serang',
	'DKI Jakarta' : 'Jakarta',
	'West Java' : 'Bandung',
	'Central Java' : 'Semarang',
	'East Java' : 'Surabaya',
	'DI Yogyakarta' : 'Yogyakarta'
}

# 2.
# copy(): a shallow copy of D
states2 = states.copy()
print "A copy of states: ", states2

# clear(): remove all items from D
states2.clear()
print "Empty states2: ", states2
states2 = states.copy()

# get(k): D[k] if k is in D, else None
print "What's the abbreviation for Oregon?", states2.get('Oregon')

# has_key(k): True if D has a key k, else False
print "Does 'Oregon' state exist?", states2.has_key('Oregon')

# items(): list of D's (key, value) pairs, as 2 tuples
print "What do we have so far?", states2.items()

# iteritems(): an iterator over the (key, value) items of D
# iterkeys(): an iterator over the keys of D
# itervalues(): an iterator over the values of D

# keys(): list of D's keys
print "What states do we have?", states2.keys()

# pop(k[, d]): remove specified key and return the corresponding value. I
# If key is not found, d is returned if given, else KeyError is raised
print "What's the capital of Oregon?", states2.pop('Oregon')
print "What's the capital of Texas?", states2.pop('Texas', 'We do not know yet')

# popitem(): remove and return some (k, v) pair as a 2-tuple
# If D is empty, raise KeyError
print "What's the first state on our list?", states2.popitem()

# setdefault(k[ ,d]): D.get(k,d)
# If k is not in D, set D[k]=d
states2.setdefault('Texas', 'TX')
print states2 # include Texas, Austin at end of list

# update([E, ]**F)

# values(): list of D's values
print "Values: ", states2.values()

# viewitems(): a set-like object providing a view on D's items
# viewkeys(): a set-like object providing a view on D's keys
# viewvalues(): an object providing a view on D's values
print "View items: ", states2.viewitems()
print "View keys: ", states2.viewkeys()
print "View values: ", states2.viewvalues()