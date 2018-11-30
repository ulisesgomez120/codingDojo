class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display_info(self):
        print(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
            return self
        return self
bike1 = Bike(150,15)
bike2 = Bike(200,20)
bike3 = Bike(250,25)

bike1.ride().ride().ride().reverse().display_info()
bike2.ride().ride().reverse().reverse().display_info()
bike3.reverse().reverse().reverse().display_info()

# would use an if statement. emonstrated above
# all methods here return self