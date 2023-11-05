#  _____                _                 _              _____   _____
# / ____|              | |               | |      /\    |  __ \ |  __ \
#| |       ___   _ __  | |_   __ _   ___ | |_    /  \   | |__) || |__) |
#| |      / _ \ | '_ \ | __| / _` | / __|| __|  / /\ \  |  ___/ |  ___/
#| |____ | (_) || | | || |_ | (_| || (__ | |_  / ____ \ | |     | |
# \_____| \___/ |_| |_| \__| \__,_| \___| \__|/_/    \_\|_|     |_|
#
# v1 by Geoffrey


from contact import Contact
import os

class DataHandler(object):

    #check if file exists
    if os.path.exists("temp_data.txt") == False:
        open('temp_data.txt','w').close()

    contacts = []
    with open ('temp_data.txt' ,encoding="utf- 8") as fp:
            for line in fp:
                name, phoneNumber,email = line.split('|')
                contact = Contact(name,phoneNumber,email.removesuffix('\n'))
                contacts.append(contact)


    def __init__(self):
        pass

    #get all
    def getAll ():
        """
        Clears the contacts list and reads in contacts from a file.
        
        Returns:
            list: A list of Contact objects representing the contacts read from the file.
        """
        DataHandler.contacts.clear()
        #read in contacts
        with open ('temp_data.txt', encoding="utf- 8") as fp:
            for line in fp:
                name, phoneNumber,email = line.split('|')
                contact = Contact(name,phoneNumber,email.removesuffix('\n'))
                DataHandler.contacts.append(contact)
                
        return DataHandler.contacts

  
    def addContact(contact):
        """
        Adds a contact to the list of contacts and writes the updated list to a file.

        Parameters:
            contact (Contact): The contact object to be added.

        Returns:
            None
        """
        DataHandler.contacts.append(contact)
        #write to file
        with open('temp_data.txt','w', encoding="utf-8") as fp:
            for contact in DataHandler.contacts:
                fp.write(f"{contact.name}|{contact.phoneNumber}|{contact.email}\n")


   
    def getSpecificContact (searchName):
        """
        Get a specific contact from the list of contacts based on the given search name.

        Parameters:
            searchName (str): The name of the contact to search for.

        Returns:
            Contact: The contact object if found, None otherwise.
        """
        for contact in DataHandler.contacts:
            if contact.getName().lower().strip() == searchName.lower().strip():
                return contact
            else :
                return None

    #verifyName? for duplicate?
    def checkIfNameExists (name):
        """
        Check if a given name exists in the list of contacts.

        Parameters:
            name (str): The name to check.

        Returns:
            str: "exists" if the name exists in the list of contacts, "ok" otherwise.
        """
        for contact in DataHandler.contacts:
            if contact.getName == name:
                return "exists"
            else:
                return "ok"

    def deleteContact(selection):
        """
        Deletes a contact from the list of contacts.
    
        Parameters:
            selection (int): The index of the contact to be deleted.
    
        Returns:
            None
        """
        del DataHandler.contacts[selection]
        with open('temp_data.txt','w', encoding="utf-8") as fp:
            for contact in DataHandler.contacts:
                fp.write(f"{contact.name}|{contact.phoneNumber}|{contact.email}\n")

    def updateContact(selection, contact):
        """
        Updates a contact in the DataHandler.
    
        Args:
            selection (int): The index of the contact to be updated.
            contact (Contact): The updated contact object.
    
        Returns:
            None
        """
        contactToUpdate = DataHandler.contacts[selection]
        contactToUpdate.setName(contact.getName())
        contactToUpdate.setPhoneNumber(contact.getPhoneNumber())
        contactToUpdate.setEmail(contact.getEmail())

        with open('temp_data.txt','w', encoding="utf-8") as fp:
            for contact in DataHandler.contacts:
                fp.write(f"{contact.name}|{contact.phoneNumber}|{contact.email}\n")
