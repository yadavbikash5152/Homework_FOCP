def calculate_pizza_price():
    """Calculates the total price of a pizza order based on BPP's pricing rules."""

    base_price = 12  # Price per pizza
    delivery_charge = 2.50  # Delivery charge (if applicable)

    # Get user input with validation
    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas > 0:
                break
            else:
                print("Please enter a positive integer for the number of pizzas.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    is_delivery = input("Is delivery required? (y/n) ").lower() == "y"
    is_tuesday = input("Is it Tuesday? (y/n) ").lower() == "y"
    used_app = input("Did the customer use the app? (y/n) ").lower() == "y"

    # Calculate base price
    total_price = base_price * num_pizzas

    # Apply Tuesday discount
    if is_tuesday:
        total_price *= 0.5

    # Add delivery charge (if applicable)
    if is_delivery and num_pizzas < 5:
        total_price += delivery_charge

    # Apply app discount (if applicable)
    if used_app:
        total_price *= 0.75

    # Display total price
    print("\nBPP Pizza Price Calculator")
    print("==========================")
    print(f"Total Price: £{total_price:.2f}")

# Call the function to start the calculator
calculate_pizza_price()
