def count_of_x_n_o(input_string):
    """
    This function counts the number of 'x' and 'o' characters in a given string.
    """
    input_string = input_string.lower()
    count_x = input_string.count('x')
    count_o = input_string.count('o')
    
    return count_x == count_o
 
 #GETTING INPUT 
input_string = input("Enter a string: ")
 
 #CALLING THE FUNCTION
result = count_of_x_n_o(input_string)
 
 #PRINTING THE OUTPUT
print(f"The number of 'x' and 'o' characters are equal: {result}")



