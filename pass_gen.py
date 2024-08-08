import random
import string

def generate_password(length):
    """
    This function generates a secure password using the random and string libraries.
    """
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


def main():
    length = int(input("Enter the desired password length (it should be greater than 8 and smaller than 17): "))
    if length < 8 or length > 17:
        print("Invalid input. Password length should be greater than 8 and smaller than 17.")
    if length == 106:
        print("paswords lenght shouldn't be boobies.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")
    
if __name__ == "__main__":
    main()

