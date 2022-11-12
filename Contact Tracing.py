print(f"\n{'=' * 75}")
print(f"{'|'}{' ': >20}{'Programmed by Irel Kian C. Bacolod'}{' ': >19}{'|'}")
print(f"{'=' * 75}")

# Create an empty dictionary
slot_dict = {
    "name": {
        "number": "info",
        "address": "info",
        "condition": "info",
        "contact-with-covid-19?": "info"},
}

contacts ={

}

def creating_database(x, y, z, a):
    slot_dict["name"]=x
    for i in x:
        x["number"] = y
        x["number"] = z
        x["number"] = a
    
    contacts[x] = y, z, a


# Display the Menu (add item, search, exit)
print("\n\n" + " " * 2  + "<" * 19 + " MENU " + ">" * 19)
print("\n[a] Add a contact", end="        ")
print("[b] Search an existing contact")
print("[c] Exit program")

# Prompt the user about the options
# Option 1 (add user information such as full name, contacts, address, etc.)
# Option 2 (search user user based on address, full name, or previous record)
# Option 3 (Ask the user if want to exit)
# Create a Loop 