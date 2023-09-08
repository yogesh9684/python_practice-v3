class Car(object):
    def __init__(self):
        print("Created Car Instance")

    def price(self):
        print("prise of the Car is 20Lac")

    def model(self):
        print("model of the car is YourChoice")

class HyundaiVenue(Car):
    def __init__(self):
        Car.__init__(self)
        print("Created Hyundai Venue Instance")

    def model(self):
        print("Model has the BMW")

c1 = Car()
c1.price()
c1.model()

b1 = HyundaiVenue()
b1.price()
b1.model()
