from contacts import Contacts
import time
import os

# Simulate the PhoneBook functions
# - Display Contacts
# - Add Contacts
# - Delete Contacts
# - Search Contacts
# - Exit

# Declare an empty list
contactList = list()

# validate the input of the user if a number
def input_validation(num):
    try:
        int(num)
    except:
        print('Invalid Input')
        get_input('Input: ')
    
    return num

# get input
def get_input(message):
    return input(message)

# display the possible options that simulates a contacts
def display_options():
    print("*"*30 + 
        "\nWelcome to Phonebook Master" +
        "\n\t[1] Display All Contacts" + 
        "\n\t[2] Add to Contacts" + 
        "\n\t[3] Delete Contacts" + 
        "\n\t[4] Search Contacts" + 
        "\n\t[5] Exit\n" + 
        "*"*30)

    # get user input for choice
    choice = input_validation(get_input('Input: '))

    # execute a respective function depending on the user input
    if choice == '1':
        os.system('cls')
        time.sleep(0.5)
        display_contact()
    elif choice == '2':
        os.system('cls')
        time.sleep(0.5)
        add_contact()
    elif choice == '3':
        os.system('cls')
        time.sleep(0.5)
        delete_contact()
    elif choice == '4':
        os.system('cls')
        time.sleep(0.5)
        search_contact()
    elif choice == '5':
        pass
    else:
        print('Invalid Input')
        os.system('cls')
        time.sleep(0.5)
        display_options()

# lets the user display all contacts    
def display_contact():
    if len(contactList) == 0:
        print('No Contacts Found')
        display_options()
    else:
        for c in contactList:
            c.display_details()

    
    display_options()

# lets the user add contact by appending to the list
def add_contact():
    print('Input Details')
    time.sleep(5)
    name = input('Enter Name: ')
    number = input('Enter Number: ')

    # validates whether the user has entered a detail of not
    if name == '' or number == '':
        print('Please Enter the needed details!')
        time.sleep(2)
        os.system('cls')
        add_contact()
    else:
        newContact = Contacts(name, number)
        contactList.append(newContact)
        os.system('cls')
        print('Adding to Contacts...')
        time.sleep(2)

    display_options()

# lets the user delete a specific person in a contact
def delete_contact():
    not_found = False
    to_delete = input('Enter Name: ')
    for names in contactList:
        if names.name.lower() == to_delete.lower():
            contactList.remove(names)
        else:
            not_found = True
    
    # validates whether the input is in the list or not
    if not_found == True:
        print(f'{to_delete} Not Found')
        time.sleep(1)
        os.system('cls')
        display_options()
    else:
        time.sleep(2)
        display_options()

# searches through the list if the input is already in the list or not
def search_contact():
    not_found = False
    search_for = input('Search for: ')
    for names in contactList:
        if names.name.lower() == search_for.lower():
            names.display_details()
        else:
            not_found = True
    
    if not_found == True:
        print(f'{search_for} Not Found')
        time.sleep(1)
        os.system('cls')
        display_options()
    else:
        time.sleep(2)
        display_options()

    pass

if __name__ == "__main__":
    display_options()

