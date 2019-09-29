"""
maps_dict.py

In Python, the map concept appears as a built-in data type called a dictionary.
A dictionary contains key-value pairs.
"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia'] = {'India': ['Bangalore']}
locations['North America']['USA'].append('Atlanta')
locations['Africa'] = {'Egypt': 'Cairo'}
locations['Asia'].update( {'China': ['Shanghai']} )
locations['North America'].update({'Mexico': ['Mexico City']})
locations['North America']['Mexico'].append('Guadalajara')
locations['North America']['Mexico'].append('Juárez')
locations['North America']['Mexico'].append('Guadalupe')
locations['North America']['Mexico'].append('Nuevo Laredo')

# TODO: Print a list of all cities in the USA in alphabetic order.
country_select = "Mexico"
usa_city_list = sorted(locations['North America'][country_select])

# print (usa_city_list)
print("="*25)

for city in usa_city_list:
    print (city)
print("="*25)

import operator
asia_city_list = []

# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
for country, cities in locations['Asia'].items():
    # print(cities, country)
    asia_city_list.append(cities[0] + ', ' + country)

# sort list on multiple attributes
asia_sorted = sorted(asia_city_list, key = operator.itemgetter(1, 2))
# print(asia_sorted)

for val in asia_sorted:
    print(val)

# print(locations)
