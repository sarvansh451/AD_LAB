class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def greet(self):
        print("make =", self.make)
        print("model =", self.model)
        print("year =", self.year)


vehicle1 = Vehicle("sedan", "high", 2000)
vehicle2 = Vehicle("EV", "low", 2004)
vehicle1.greet()
vehicle2.greet()


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def greet(self):
        super().greet()
        print("num_doors =", self.num_doors)
        print("fuel_type =", self.fuel_type)


d = Car("SUV", "mid", 2020, 4, "petrol")
d.greet()
