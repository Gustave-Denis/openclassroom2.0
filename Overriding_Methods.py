class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Chuff")

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg,"\
            f" has a lifespan of {self.lifespan_in_years} years and "\
            f"can run at a maximum speed of {self.speed_in_kph}kph."


class Tiger(Cat):
    def __init__(self, mass, lifespan, speed, coat_pattern = "striped"):
        self.coat_pattern = coat_pattern
        super().__init__(mass, lifespan, speed)

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg,"\
            f" has a lifespan of {self.lifespan_in_years} years "\
            f"and can run at a maximum speed of {self.speed_in_kph}kph."\
            f" It also has a {self.coat_pattern} coat."


# This code is used to test your class
if __name__ == '__main__':
    tiger = Tiger(310, 26, 65,"striped")
    print(tiger)
