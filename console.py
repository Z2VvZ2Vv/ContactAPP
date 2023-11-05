#  _____                _                 _              _____   _____
# / ____|              | |               | |      /\    |  __ \ |  __ \
#| |       ___   _ __  | |_   __ _   ___ | |_    /  \   | |__) || |__) |
#| |      / _ \ | '_ \ | __| / _` | / __|| __|  / /\ \  |  ___/ |  ___/
#| |____ | (_) || | | || |_ | (_| || (__ | |_  / ____ \ | |     | |
# \_____| \___/ |_| |_| \__| \__,_| \___| \__|/_/    \_\|_|     |_|
#
# v1 by Geoffrey


from data_handler import *
from contact import *
import itertools

#Efface l'écran de la console.
def cls():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name=='nt' else 'clear')

def logo():
    cls()
    print("  _____                _                 _              _____   _____")
    print(" / ____|              | |               | |      /\    |  __ \ |  __ \ ")
    print("| |       ___   _ __  | |_   __ _   ___ | |_    /  \   | |__) || |__) |")
    print("| |      / _ \ | '_ \ | __| / _` | / __|| __|  / /\ \  |  ___/ |  ___/")
    print("| |____ | (_) || | | || |_ | (_| || (__ | |_  / ____ \ | |     | |")
    print(" \_____| \___/ |_| |_| \__| \__,_| \___| \__|/_/    \_\|_|     |_|")
    print()

contacts = []

#switch cases and main
def main():
    """
    Runs the main menu loop of the ContactAPP.

    This function displays a menu and prompts the user to select an option.
    The available options are:
    1. View all contacts
    2. Add a new contact
    3. Delete a contact
    4. Update a contact
    5. Search for a contact
    6. Exit the program

    The function continues to display the menu and prompt for a selection
    until the user chooses option 6 to exit the program.

    Parameters:
    None

    Returns:
    None
    """
    selection = None
    while selection != 6:
        selection = menuSelection()
        if selection == 1: 
                viewAllContacts()
        elif selection == 2:
                addNewContact()
        elif selection == 3:
                deleteContact()
        elif selection == 4:
                updateContact()
        elif selection == 5:
                searchForContact()
    logo()
    print("--------------------------------------------------------")
    print("Thanks for using ContactAPP, goodbye :)")
    print("--------------------------------------------------------")
    print()


#menu selection

def menuSelection ():
    """
    Displays a menu and prompts the user for a selection.
    
    Returns:
        int: The user's selection as an integer.
    """
    logo()
    print("--------------------------------------------------------")
    print("Welcome to the ContactAPP menu, what would you like to do?")
    print()

    print("1: View full list of contacts")
    print("2: Add new contact")
    print("3: Delete a contact")
    print("4: Update a contact")
    print("5: Search for a contact")
    print("6: Quit the application")
    print()
    
    while True:
        print("Enter a number corresponding to the above menu and then press ENTER")
        print()
        selection = input("")
        print()

        try:
            selectionToInt = int(selection)

            if selectionToInt < 7 and selectionToInt > 0:
                return selectionToInt
            else:
                print ("Sorry that number does not exist in the above menu, please choose again")
        except ValueError:
            print(f"""Sorry, "{selection}" is not a number. Please choose anumber from the menu""")



def viewAllContacts ():
    """
    View all contacts and display them in a formatted table.

    This function retrieves all contacts from the data handler and displays them in a formatted table.
    The table includes the contact's name, phone number, and email.

    Parameters:
    None

    Returns:
    None
    """
    logo()
    print("--------------------------------------------------------")
    print("Full contacts list")
    print("--------------------------------------------------------")
    print("")

    contacts = DataHandler.getAll()

    print("| NAME | PHONE NUMBER | EMAIL |")
    print()
    if len(contacts) != 0:
        for contact in contacts:
            print(contact)
    else:
        print("You do not have any contacats yet!")
        print()

    print()
    input("Press ENTER to return to the main menu")
    return None
    

def addNewContact():
    """
    Adds a new contact to the system.

    This function prompts the user to enter a name for the contact and then waits for the user to press the ENTER key to submit the name. If the name entered is empty, an error message is displayed and the user is prompted to enter a name of at least one character.

    After the name is entered, the function prompts the user to enter a phone number. If the user wishes to leave the phone number empty, they can simply press ENTER.

    Next, the function prompts the user to enter an email address. If the user wishes to leave the email address empty, they can simply press ENTER.

    Based on the entered values, a new Contact object is created with the given name, phone number, and email address. If both the phone number and email address are empty, default values are used.

    The new Contact object is then added to the system using the DataHandler.addContact() method.

    Parameters:
    None

    Returns:
    None
    """
    logo()
    print("--------------------------------------------------------")
    print("Add a new contact")
    print("--------------------------------------------------------")
    print("")

    while True:
        print("please enter a name and then press the ENTER key to submit")
        name = input("")
        print()

        if len(name) == 0:
            print("Sorry, no name was entered, please enter a name of at least one character")
            print()
        else:
            print("Now please enter a phone number.")
            print("If you wish to leave the phone number empty, just press ENTER")
            phoneNumber = input()

            print()
            print("Now please enter an email address.")
            print("If you wish to leave the email address empty, just press ENTER")
            email = input()
            print()

            if email == "" and phoneNumber == "":
                contact = Contact(name, "no number supplied", "no email supplied")
            elif email == "" and phoneNumber !="":
                contact = Contact(name, phoneNumber, "no email supplied")
            elif email != "" and phoneNumber =="":
                contact = Contact(name, "no number supplied", email)
            else:
                contact = Contact(name,phoneNumber,email)

            DataHandler.addContact(contact)
            return None


def deleteContact():
    """
    Deletes a contact from the contact list.

    This function prompts the user to select a contact from the list of contacts. If the user selects a valid contact, it is deleted from the contact list. If the user does not select a valid contact, no contact is deleted.

    Parameters:
    None

    Returns:
    None
    """
    logo()
    print("--------------------------------------------------------")
    print("Delete a contact")
    print("--------------------------------------------------------")
    print()

    contacts = DataHandler.getAll()

    if len(contacts)== 0:
        print("You do not have any contacats yet!")
        print()
        print()
        input("Press ENTER to return to the main menu")
        return None

    for i,contact in zip(itertools.count(),contacts):
        print(f"{i}: {contact}")
    print("--------------------------------------------------------")
    print()

    print("Select the number of the contact you would like to delete and press ENTER")
    print("To return back, please enter 'exit' !")
    print()
    inputString = input("")
#need while loop to ensure int input
    if inputString == 'exit':
        return None

    selection = int(inputString)

    if selection >=0 and selection < len(contacts):
        print("contact: " + contacts[selection].getName() + " has been deleted")
        DataHandler.deleteContact(selection)   
        print()
    else:
        print("selection invalid, no contacts have been deleted")
        print()
    return None


def updateContact ():
    """
    Updates a contact in the contact list.

    This function prompts the user to select a contact from the list of contacts
    and allows them to update the contact's name, phone number, and email address.

    Parameters:
    None

    Returns:
    None
    """
    logo()
    print("--------------------------------------------------------")
    print("Update a contact")
    print("--------------------------------------------------------")
    print("")

    contacts = DataHandler.getAll()

    if len(contacts)== 0:
        print("You do not have any contacats yet!")
        print()
        print()
        input("Press ENTER to return to the main menu")
        return None

    for i,contact in zip(itertools.count(),contacts):
        print(f"{i}: {contact}")
    print("--------------------------------------------------------")

    print()
    print("Select the number of the contact you would like to update and press ENTER")
    print("To return back, please enter 'exit' !")
    print()

    while True:
        inputString = input("")
        
        if inputString == 'exit':
            return None
        
        selection = int(inputString)

        if selection >-1 and selection < len(contacts):
            contact = contacts[selection]
            print("contact to update is:")
            print(contact)
            print()
            
            print("Please enter a new name and press the ENTER key to submit")
            print("If you don't wish to change the name, just press ENTER")
            print()
            name = input("")
            print()

            if len(name) == 0:
                print("Ok, name will not be changed")
                print()
            else:
                print("Thanks, name will be changed to: " + name)
                print()
                contact.setName(name)

            print("Now please enter a phone number.")
            print("If you wish to leave the phone number empty, just press ENTER")
            print()
            phoneNumber = input()
            print()

            if len(phoneNumber) == 0:
                print("Ok, phone number will not be changed")
                print()
            else:
                print("Thanks, phone number will be changed to: " + phoneNumber)
                print()
                contact.setPhoneNumber(phoneNumber)

            print("Now please enter an email address.")
            print("If you wish to leave the email address empty, just press ENTER")
            print()
            email = input()
            print()

            if len(email) == 0:
                print("Ok, email will not be changed")
                print()
            else:
                print("Thanks, email will be changed to: " + email)
                print()
                contact.setEmail(email)


            DataHandler.updateContact(selection,contact)
            return None

        else:
            print("selection invalid, please re-enter")
            print()


def searchForContact ():
    """
    This function allows the user to search for a contact in the contact list.
    It displays a menu with a list of contacts and prompts the user to enter a name to search for.
    If the user enters '0', the function returns None.
    If a contact with the entered name exists, it displays the contact's details.
    If no contact with the entered name exists, it displays a message indicating that no contacts exist with that name.
    """
    logo()
    print("--------------------------------------------------------")
    print("Search for a contact")
    print("--------------------------------------------------------")
    print("")

    contacts = DataHandler.getAll()

    if len(contacts)== 0:
        print("You do not have any contacats yet!")
        print()
        print()
        input("Press ENTER to return to the main menu")
        return None

    print("Please enter a name to search for")
    print("To return back, please enter '0' !")
    print()

    while True:
        inputName = input("")
        print()

        if inputName == '0':
            return None

        contact = DataHandler.getSpecificContact(inputName)

        if contact is None:
            print("Sorry, no contacts exist with that name")
            print()
        else:
            print("Contact found! Here are their details:")
            print("| NAME | PHONE NUMBER | EMAIL |")
            print()
            print(contact)
            print()
            input("Press ENTER to return to the main menu")
            return None