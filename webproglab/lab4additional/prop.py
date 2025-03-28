class Vehicle:
    """A class where all instances share the same property."""
    
    # Class variable (shared by all instances)
    wheels = 4  

    def __init__(self, brand, model):
        """Initialize instance attributes."""
        self.brand = brand
        self.model = model

# Creating multiple instances
car1 = Vehicle("Toyota", "Camry")
car2 = Vehicle("Honda", "Civic")

# Accessing the class property
print(f"🚗 {car1.brand} {car1.model} has {car1.wheels} wheels")
print(f"🚙 {car2.brand} {car2.model} has {car2.wheels} wheels")

# Modifying the class variable affects all instances
Vehicle.wheels = 6  
print(f"🛻 {car1.brand} {car1.model} now has {car1.wheels} wheels")
print(f"🚌 {car2.brand} {car2.model} now has {car2.wheels} wheels")
