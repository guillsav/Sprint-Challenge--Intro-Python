from csv import reader

cities = []


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str_(self):
        return f"<City:{self.name} {self.lat} {self.lon}>"


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    with open("cities.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)
        for c in csv_reader:
            name = c[0]
            lat = c[3]
            lon = c[4]
            c = City(name, lat, lon)
            # cities.append(c)
    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(f"{c.name, c.lat, c.lon}")
