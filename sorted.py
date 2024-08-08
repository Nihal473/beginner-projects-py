def sorted_number(numbers, order):
    """
    This function takes in a list of numbers and a sorting order (ascending or descending) as input.
    It returns a new list containing the numbers sorted in the specified order.
    the order perameter takes 3 arguments "asc, desc, and none."
    """
    if order == "asc":
        sorted_numbers = sorted(numbers)
    elif order == "desc":
        sorted_numbers = sorted(numbers, reverse=True)
    elif order == "none":
        sorted_numbers = numbers
    else:
        return "invalid perameter for order. use 'asc' or 'desc'."

    return sorted_numbers

#GETTING INPUT
numbers_input = input('Which numbers do you want to sort (separated by spaces): ')
order = input('In which order do you want to sort (asc, desc, none): ')


##converting strings input to integers
numbers = list(map(int, numbers_input.split()))

#printing sorted numbers
print(sorted_number(numbers, order))
