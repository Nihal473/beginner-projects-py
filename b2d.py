def decimal_to_binary(decimal_number):
    """
    This function converts a decimal number to its binary representation.
    """
    # Convert decimal to binary using bitwise operators
    binary = ""
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary
        decimal_number //= 2

    return binary

while True:
    try:
        # getting input from the user
        decimal_number = int(input("Enter a decimal number (less than 1,024): "))

        # error handling for valid range
        if decimal_number < 0 or decimal_number > 1023:
            print("Invalid input. Please enter a decimal number (less than 1,024).")
            continue
        else:
            # Convert decimal to binary
            binary_number = decimal_to_binary(decimal_number)
            # print decimal
            print(f"{decimal_number} in binary is: {binary_number}")
            break  # exit the loop if a valid input is given
        
    except ValueError:
        # handles non-int values
        print("Error: Please enter a valid integer.")

        
    
