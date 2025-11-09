class PhoneBook:
    phone_directory=[]
    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        PhoneBook.phone_directory.append(self)


    def show_contact(self):
        return f"Name:{self.name}, Contact number:{self.phone}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("NO contact found in the directory")
        else:
            for contact in cls.phone_directory:
                print(contact)



    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone

        return f"No contact found for {search_name}"

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) >= 8 and phone_number.isdigit():
            return True
        else:
            return False
n_contact= int (input("How many contacts do you want to add? "))
for i in range(n_contact):
    name = input("Enter the name of the contact:")
    phone_number = input("Enter the phone number:")
    if PhoneBook.validate_phone_number(phone_number):
        PhoneBook(name,phone_number)
    else:
        print(f"Invalid phone number for {name},{phone_number}")

# c1 = PhoneBook("jon",98745612387)
# c2 = PhoneBook("jack",9956487859)
# print(PhoneBook.phone_directory)
# print(c1.show_contact())
# print(c2.show_contact())
#
# c1.show_all_contact()
# c2.show_all_contact()
#
# print(PhoneBook.search_contact("jack"))
# print(PhoneBook.search_contact("mark"))



