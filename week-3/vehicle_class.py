class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors  # made private

    def get_num_doors(self):
        return self.__num_doors

    def describe(self):  # polymorphism
        return (f"Car - Make: {self.make}, Model: {self.model}, Number of Doors: {self.__num_doors}")

class Bike(Vehicle):
    def __init__(self, make, model, num_wheels):
        super().__init__(make, model)
        self.num_wheels = num_wheels

    def describe(self):  # polymorphism
        return (f"Bike - Make: {self.make}, Model: {self.model}, Number of Wheels: {self.num_wheels}")

def main():
    car = Car('Toyota', '1435', 2)
    bike = Bike('Tesla', 'Electric', 3)

    print(car.describe())
    print(bike.describe())

main()
