import os

FILENAME = "contacts.txt"

def add_contact(name, phone):
    
    with open(FILENAME, "a") as file:
        file.write(f"{name},{phone}\n")
    print(f"Contact '{name}' added.")

def list_contacts():
    
    if not os.path.exists(FILENAME):
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    with open(FILENAME, "r") as file:
        for line in file:
            # Strip removes the newline character
            parts = line.strip().split(",")
            if len(parts) == 2:
                print(f"Name: {parts[0]} | Phone: {parts[1]}")
    print("--------------------\n")

if __name__ == "__main__":
    # Test the functions
    add_contact("Maryam", "123-456-7890")
    add_contact("Instructor", "987-654-3210")
    list_contacts()