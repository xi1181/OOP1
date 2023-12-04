class Car:
    def __init__(self, br, col, drs):
        self.brand = br
        self.color = col
        self.doors = drs


var1 = Car("Toyota", "Red", 4)
var2 = Car("BMW", "Black", 2)

print(var1.brand)
print(var2.brand)