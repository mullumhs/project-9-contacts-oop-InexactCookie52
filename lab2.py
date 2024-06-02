"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.
class Contact:
    num_of_contacts = 0
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        Contact.num_of_contacts += 1
        
contact1 = Contact("John D", "04 137 844 948", "johndoe@gmail.com")
contact2 = Contact("Jane D", "04 128 860 264", "janedoe@gmail.com")
# Create at least two instances of the Contact class with different data.



# Write code that prints out the details of each contact you have created.
print(f"number of contacts = {Contact.num_of_contacts}")
print(contact1. name, contact1.email, contact1.phone_number)
print(contact2. name, contact2.email, contact2.phone_number)
