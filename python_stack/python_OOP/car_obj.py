class Car:
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = lambda: .12 if self.price < 10000 else .15
        def display_all(self):
            print(f"price: {self.price}")
            print(f"Speed: {self.speed}")
            print(f"Fuel: {self.fuel}")
            print(f"Mileage: {self.mileage}")
            print(f"Tax: {self.tax()}")
            return self
        display_all(self)
            
    
car1 = Car(2000,"35mph","Full","15mpg")
car2 = Car(2000,"5mph","Not Full","105mpg")
car3 = Car(2000,"15mph","Kind of Full","95mpg")
car4 = Car(2000,"25mph","Full","25mpg")
car5 = Car(2000,"45mph","Empty","15mpg")
car6 = Car(20000000,"35mph","Full","15mpg")