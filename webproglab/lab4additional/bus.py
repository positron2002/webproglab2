# Parent class
class Vehicle:
    def __init__(self, brand, model, year):
        """Initialize Vehicle attributes"""
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Displays vehicle details"""
        print(f"🚗 Vehicle: {self.year} {self.brand} {self.model}")

# Child class (inherits from Vehicle)
class Bus(Vehicle):
    def __init__(self, brand, model, year, capacity):
        """Initialize Bus-specific attributes and inherit from Vehicle"""
        super().__init__(brand, model, year)
        self.capacity = capacity

    def display_info(self):
        """Displays bus details (overrides parent method)"""
        super().display_info()  # Call parent class method
        print(f"🚌 Bus Capacity: {self.capacity} passengers")

# Creating an instance of Bus
school_bus = Bus("Tata", "Starbus", 2022, 50)

# Calling method
school_bus.display_info()
