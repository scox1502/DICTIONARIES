pets = []
people = []
cities = []

pet1 = {
	'type of animal':'cat',
	'name':'William',
	'owner':'samuel', }
pets.append(pet1)

pet2 = {
    'type of animal':'cat',
	'name':'timbit',
	'owner':'troy', }
pets.append(pet2)

pet3 = {
	'type of animal':'hamster',
	'name':'vera',
	'owner':'mickeal', }
pets.append(pet3)
for pets in pets:
	print(f"{pets}")

people1 = {
	'first name':'samuel',
	'last name':'cox',
	'phone number':'236 515 5475', }
people.append(people1)

people2 = {
	'first name':'Dwayne',
	'last name':'Johnson',
	'phone number':'203-989-3399', }
people.append(people2)

people3 = {
	'first name':'Thomas',
	'last name':'Holland',
	'phone number':'913-829-2372', }
people.append(people3)
for people in people:
	print(f"{people}")

city1 = {
	'city name':'north delta',
	'estimated population':'60,769',
	'country':'Canada',
	'fact':'it is the biggest municipality in the GVRD', }
cities.append(city1)

city2 = {
	'city name':'tokyo',
	'estimated population':'37.4 million',
	'country':'japan',
	'fact':'Tokyo has the most Michelin-starred restaurants in the world', }
cities.append(city2)

city3 = {
	'city name':'new york',
	'estimated population':'8,097,282',
	'country':'the united states of amarica',
	'fact':'More than 800 languages are spoken in New York City', }
cities.append(city3)
for cities in cities:
	print(f"{cities}")