# Initialize an empty list to store contacts
contacts = []

def add_contact(name, email, contact):
    """
    This function adds a new contact to the contacts list.
    """
    contact = (name, email, contact)
    contacts.append(contact)
    print("Contact added successfully!")

def delete_contact(name):
    """
    This function deletes a contact from the contacts list by their name.
    """
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            contacts.pop(i)
            print(f"Contact '{name}' deleted successfully!")
            return
    print(f"Contact '{name}' not found.")

def search_contact(name):
    """
    This function searches for a contact by their name and returns their details.
    """
    for contact in contacts:
        if contact[0] == name:
            return contact
    print(f"Contact '{name}' not found.")

def view_contact():
    """
    This function displays all the contacts in the contacts list.
    """
    if contacts:
        print("Contact List:")
        for contact in contacts:
            print(f"{contact[0]} - {contact[1]} - {contact[2]}")
    else:
        print("No contacts found.")
        return
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View Contacts")
        print("6. Exit")
        choice = input("Enter your choice (1-5): ")
    
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            contact = input("Enter contact number: ")
            add_contact(name, email, contact)
        elif choice == "2":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "3":
            name = input("Enter name to search: ")
            result = search_contact(name)
            if result:
                print(f"Name: {result[0]}")
                print(f"Email: {result[1]}")
                print(f"Contact: {result[2]}")
            else:
                print("Contact not found.")
        elif choice == "4":
            view_contact()
        elif choice == "5":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

