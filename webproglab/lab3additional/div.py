def DivExp(a, b):
    """Performs division a/b with validation."""
    assert a > 0, "Error: 'a' must be greater than 0"  # Assertion to ensure a > 0

    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed!")  # Raise exception for b = 0

    return a / b  # Perform division

# Read input values from the user
try:
    a = float(input("Enter a positive number (a): "))
    b = float(input("Enter a non-zero number (b): "))

    # Call function and display result
    result = DivExp(a, b)
    print(f"✅ Result: {a} / {b} = {result}")

except AssertionError as ae:
    print(f"❌ Assertion Error: {ae}")

except ZeroDivisionError as zde:
    print(f"❌ Zero Division Error: {zde}")

except ValueError:
    print("❌ Invalid input! Please enter numeric values.")
