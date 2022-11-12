print(f"\n{'=' * 75}")
print(f"{'|'}{' ': >20}{'Programmed by Irel Kian C. Bacolod'}{' ': >19}{'|'}")
print(f"{'=' * 75}")

# Create an empty dictionary
contacts ={
     

}

def creating_database(w,x, y, z, a, b):
    contacts[w] = {
        "age": x,
        "number": y,
        "address": z,
        "cough/cold/fever?": a,
        "contact-with-covid-19?": b}


# Display the Menu (add item, search, exit)
print("\n\n" + " " * 2  + "<" * 19 + " MENU " + ">" * 19)
print("\n[a] Add a contact", end="        ")
print("[b] Search an existing contact")
print("[c] View Directory", end="       ")
print("[d] Exit")

while True:
    # Prompt the user about the options
    option = input("\nChoose an option from (a-c): ")
    
    # Option 1 (add user information such as full name, contacts, address, etc.)
    if option.lower() == "a":
        print("\nPlease fill up the necessary information for contact tracing.")
        name = input("Enter your full name: ")
        age = input("Enter your age: ")
        number = input("Enter your number: ")
        address = input("Enter your address: ")
        condition =input("Are you experiencing cough, cold, or fever? (yes/no): ")
        in_contact = input("Do you had contact with a person with Covid? (yes/no): ")
        creating_database(name, age, number, address, condition, in_contact)
        print("\nDATA SAVED SUCCESSFULLY!!!")

    # Option 2 (search user record)
    elif option.lower() == "b":
        search = input("\nEnter name you wanted to search: ")
        for list in contacts:
            if list == search:
                print("age:", contacts[search]["age"])
                print("number:", contacts[search]["number"])
                print("address:", contacts[search]["address"])
                print("cough/cold/fever:", contacts[search]["cough/cold/fever?"])
                print("contact-with-covid-19:", contacts[search]["contact-with-covid-19?"])
            


    # Option 3 (View all contacts)
    elif option.lower() == "c":
        print()
        print("Based on the database, {} persons are listed below:\n".format(str(len(contacts))))
        for i in contacts:
            print(i)



    # Option 4 (Ask the user if want to exit)
    elif option.lower() == "d":
        retry = input("\nDo you want to continue?(y/n) ")
        if retry.lower() == "y":
            continue
        elif retry.lower() == "n":
            break
    # Create a Loop 
    else:
        print("invalid input!!!")
        continue
    print("\n----------------------Line Break----------------------------")