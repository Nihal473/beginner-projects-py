def hide_creditcard_number(credit_card_number):
    """
    This function hides the credit card number by replacing the last four digits with asterisks.
    """
    return f"************{credit_card_number[-4:]}"

#getting input from the user
credit_card_number = input("Enter your credit card number: ")
    
# Validate the credit card number
if len(credit_card_number) != 16 or not credit_card_number.isdigit():
    print("Invalid credit card number. Please enter a 16-digit number.")
else:
    # Hide the credit card number
    hidden_number = hide_creditcard_number(credit_card_number)
    print(f"Your hidden credit card number is: {hidden_number}")