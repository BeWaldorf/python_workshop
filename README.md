# python_workshop

python workshop stappenplan voor ppt

class Animal:
    def __init__(self, name, color, breed, age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
        
    def attack(self):
        pass # implemented in child classes

class Cat(Animal):
    def __init__(self, name, color, breed, age, mood):
        super().__init__(name, color, breed, age)
        self.mood = mood
    
    def attack(self):
        print("Scratch")
    
    def drink_milk(self):
        print("Cat is drinking")
    
    def meow(self):
        print("Meow")
        

cat1 = Cat("Pluisje", "Black", "Bengal", 12, "bored")
cat2 = Cat("Simba", "Orange", "Burmese", 8, "hyper")

cat1.name = "Ziggy"
cat1.Meow()

class Dog(Animal):
    def __init__(self, name, color, breed, age, energy_level):
        super().__init__(name, color, breed, age)
        self.energy_level = energy_level
    
    def attack(self):
        print("Bite")
    
    def bark(self):
        print("Bark Bark")
    
    def follow_postman(self):
        print("The dog chases the postman")
        