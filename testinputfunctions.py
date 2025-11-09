def inputFloat(prompt):
    """Prompt the user for a floating-point number and validate input."""
    while True:
        user_input = input(prompt)
        
        # Allow only digits or digits with a single decimal point
        if user_input.count('.') <= 1 and user_input.replace('.', '').isdigit():
            return float(user_input)
        else:
            print("Invalid input. Please enter a valid floating-point number.")


# Short tester program
print("Testing inputFloat function")
number = inputFloat("Enter a floating-point number: ")
print("You entered:", number)
