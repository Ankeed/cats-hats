# 1

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = self.name + " " + other_country.name
        combined_population = self.population + other_country.population
        new_country = Country(combined_name, combined_population)
        return new_country


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


# 2

class Country2:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = self.name + " " + other_country.name
        combined_population = self.population + other_country.population
        new_country = Country(combined_name, combined_population)
        return new_country


bosnia = Country2('Bosnia', 10_000_000)
herzegovina = Country2('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


# 3

class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def display_speed(self):
        print("Current speed:", self.speed)


    