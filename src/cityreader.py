import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
    def __repr__(self):
        return '%s: (%.2f, %.2f)' % (self.name, self.latitude, self.longitude)

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

with open('cities.csv', newline='') as csvfile:
    citiesreader = csv.reader(csvfile, delimiter=',')
    cities = []
    for city in citiesreader:
        try:
            newCity = City(city[0], float(city[3]), float(city[4]))
            cities.append(newCity)
        except ValueError:
            continue
    
# Print the list of cities (name, lat, lon), 1 record per line.

for city in cities:
    print(city)

# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

firstCoords = input("First Coordinates | Enter a latitude and longitude:\n")
x1, y1 = [coordinate for coordinate in firstCoords.split()]
x1 = float(x1)
y1 = float(y1)
print("\nYour first coordinates are %.2f,%.2f\n" % (float(x1), float(y1)))

secondCoords = input("Second Coordinates | Enter a latitude and longitude:\n")
x2, y2 = [coordinate for coordinate in secondCoords.split()]
x2 = float(x2)
y2 = float(y2)
print("\nYour second coordinates are %.2f,%.2f\n" % (float(x2), float(y2)))

print("Your Encompassed Cities are:\n")
encompassedCities = [city for city in cities 
if min(x1, x2) < city.latitude < max(x1, x2) 
and min(y1, y2) < city.longitude < max (y1, y2)]

for city in encompassedCities:
    print (city)
print("")