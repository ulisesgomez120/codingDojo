class Product:
    def __init__(self,price,item_name,weight,brand,status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = "sold"
        return self
    def returns(self, reason_for_return):
        if reason_for_return == "like_new":
            self.status = "for sale"
            return self
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
            return self
        if reason_for_return == "opened":
            self.status = "used"
            self.price = self.price - (self.price * .2)
            return self
    def add_tax(self,decimal_percentage):
        price_with_tax = self.price + (self.price * decimal_percentage)
        return f"Price with tax {price_with_tax}"
    def display_info(self,sales_tax=.08):
        print(f"\nName: {self.item_name}")
        print(f"Price: {self.price}")
        print(f"Weight: {self.weight}")
        print(f"Brand: {self.brand}")
        print(f"Status: {self.status}")
        print(self.add_tax(sales_tax))
        return self

pro1 = Product(10,"shirt",.98,"supreme")
pro1.sell().returns("opened").display_info()
