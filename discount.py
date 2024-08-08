def calculate_discounted_price(price, discount):
    """
    This function calculates the discounted price of an item based on the given price and discount percentage.
    """
    return price - (price * (discount / 100))

# Getting input parameters
price_input = input("Enter the price of the item: ")
discount_input = input("Enter the discount percentage: ")

# Error checking for price and discount being numbers
try:
    price = float(price_input)
    discount = float(discount_input)
except ValueError:
    print("Error: Please enter valid numbers for price and discount.")
    exit()

# Error checking for discount values
if discount < 0:
    print("Error: Discount percentage cannot be negative.")
elif discount > 100:
    print("Error: Discount percentage must be under 100.")
elif discount == 0:
    print("Error: Discount percentage cannot be zero.")
else:
    # Calculate discounted price
    discounted_price = calculate_discounted_price(price, discount)
    # Output the discounted price
    print("The discounted price is:", discounted_price)
