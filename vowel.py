def vowel_count(word):
    """
    This function takes a string as input and returns the count of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


# GETTING INPUT && error checking

while True:
    word = input("Please enter a word: ")

    if not word:
        print("Input cannot be empty. Please enter a valid word.")
        continue

    if word.isalpha():
        break
    
    else:
        print("Invalid input. Please enter a valid word.")



# CALLING THE FUNCTION
vowel =vowel_count(word)

#printing the output
print(f"The number of vowels in '{word}' is: {vowel}")
