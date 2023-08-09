def load_address_book():
    try:
        with open("address_book.txt", "r") as file:
            lines = file.readlines()
            return [eval(line.strip()) for line in lines]
    except FileNotFoundError:
        return []

def save_address_book(address_book):
    with open("address_book.txt", "w") as file:
        for contact in address_book:
            file.write(str(contact) + "\n")

def create_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email (optional): ")

    contact = {"name": name, "phone": phone, "email": email}
    return contact

def update_contact(address_book, name):
    for contact in address_book:
        if contact["name"] == name:
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email (optional): ")
            contact["phone"] = phone
            contact["email"] = email
            return True
    return False

def delete_contact(address_book, name):
    for contact in address_book:
        if contact["name"] == name:
            address_book.remove(contact)
            return True
    return False

def main():
    address_book = load_address_book()

    while True:
        print("\nAddress Book Menu:")
        print("1. Create new contact")
        print("2. Update existing contact")
        print("3. Delete contact")
        print("4. Display all contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            contact = create_contact()
            address_book.append(contact)
            print("Contact created successfully!")
        elif choice == "2":
            name = input("Enter the name of the contact to update: ")
            if update_contact(address_book, name):
                print("Contact updated successfully!")
            else:
                print("Contact not found!")
        elif choice == "3":
            name = input("Enter the name of the contact to delete: ")
            if delete_contact(address_book, name):
                print("Contact deleted successfully!")
            else:
                print("Contact not found!")
        elif choice == "4":
            if len(address_book) == 0:
                print("Address book is empty.")
            else:
                print("\n--- Contacts ---")
                for contact in address_book:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        elif choice == "5":
            save_address_book(address_book)
            print("Address book saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
