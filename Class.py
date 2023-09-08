class Car():
    wheels = 4
    def __init__(self,make,year):
        self.make = make
        self.year = year

    def info(self):
        print("Make of the Car is",self.make)
        print("Year of the Car is" ,self.year)

c1 = Car("Hyundai Venue N Line","2022")
c1.wheels=3
print("Car has the" ,Car.wheels,"Wheels")
c1.info()
