print(f"\n{'=' * 75}")
print(f"{'|'}{' ': >20}{'Programmed by Irel Kian C. Bacolod'}{' ': >19}{'|'}")
print(f"{'=' * 75}")

# Create an empty dictionary
contacts ={

}

def creating_database(x, y, z, a, b):
    contacts[x] = {
        "number": y,
        "address": z,
        "cough/cold/fever?": a,
        "contact-with-covid-19?": b}


# Display the Menu (add item, search, exit)
print("\n\n" + " " * 2  + "<" * 19 + " MENU " + ">" * 19)
print("\n[a] Add a contact", end="        ")
print("[b] Search an existing contact")
print("[c] Exit program")

# Prompt the user about the options
option = input("\nChoose an option from (a-c): ")

# Option 1 (add user information such as full name, contacts, address, etc.)
if option.lower() == "a":
    print("\nPlease fill up the necessary information for contact tracing.")
    name = input("Enter your full name: ")
    number = input("Enter your number: ")
    address = input("Enter your address: ")
    condition =input("Are you experiencing cough, cold, or fever? (yes/no): ")
    in_contact = input("Do you had contact with a person with Covid? (yes/no): ")
    creating_database(name, number, address, condition, in_contact)
    print(contacts)

# Option 2 (search user record)
if option.lower() == "b":
    search = input("\nEnter name you wanted to search: ")
    if search in contacts:
        print(contacts[search])

# Option 3 (Ask the user if want to exit)

# Create a Loop 