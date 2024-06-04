"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contactsc
class Contact:
    num_of_contacts = 0
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        Contact.num_of_contacts += 1
    
    def check_email(self):
        if "@" in self.email:
            print("Hello world")
            return True
        

    #classmethod: 


        
contact1 = Contact("John D", "04 137 844 948", "johndoe@gmail.com")
contact2 = Contact("Jane D", "04 128 860 264", "janedoe@gmail.com")
print(f"number of contacts = {Contact.num_of_contacts}")
print(contact1. name, contact1.email, contact1.phone_number)
print(contact2. name, contact2.email, contact2.phone_number)
contact1.check_email



☺Ö☺☺
#☺
╚