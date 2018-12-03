class Animal:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        return self
ani1 = Animal("randi",20)

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,health=150)      
    def pet(self):
        self.health += 5
        return self
Odin = Dog("Odin")

class Dragon(Animal):
    def __init__(self,name):
        super().__init__(name,health=170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super().display_health()
        print("I am a dragon")
        return self
Draegon = Dragon("Draegon")

Draegon.walk().fly().display_health()
print("\n")
Odin.walk().walk().walk().run().run().pet().display_health()
print("\n")
ani1.walk().walk().walk().run().run().display_health()
print("\n")
ani2 = Animal("randi2",50)
ani2.display_health()
# Odin.fly()
# ani2.fly()
# ani2.pet()
