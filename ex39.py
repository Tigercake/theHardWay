states = {
    'Oregon' : 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])


print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])


print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} state is abbreviated {abbrev}")
    print(F"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print('Sorry, no Texas.')

city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")
