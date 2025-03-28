class StringManipulator:
    def __init__(self):
        self.text = ""

    def get_String(self):
        """Accepts a string from the user."""
        self.text = input("Enter a string: ")

    def print_String(self):
        """Prints the string in uppercase."""
        print("Uppercase String:", self.text.upper())

# Create an instance of the class
string_obj = StringManipulator()

# Call methods
string_obj.get_String()
string_obj.print_String()
