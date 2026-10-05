class Car:
    def __init__(self,brand,colour,owner):
        self.brand = brand
        self.colour = colour
        self.owner = owner
        
car1 = Car("Toyota", "Black", "Kawsar")
car2 = Car("Tata", "White", "Habib")

print("========car1 details=========\n")
print("Brand name:",car1.brand)
print("Colour:",car1.colour)
print("owner name:",car1.owner)
print()
print("========car2 details=========\n")
print("Brand name:",car2.brand)
print("colour:",car2.colour)
print("owner name:",car2.owner)