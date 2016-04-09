class Kontakt:
    def __init__(self, first_name, last_name, email, address):
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.address = address

all_contacts = []


while True:
    add_new_contact = raw_input("Do you want to add new contact?")
    if (add_new_contact).lower() == "da" or (add_new_contact).lower() == "yes":
        object = Kontakt(first_name=raw_input("Add name"), last_name=raw_input("Add last name"), email=raw_input("Add email"), address=raw_input("Add adress"))
        all_contacts.append(object)


        print object.firstname, object.lastname, object.email, object.address

    else:
        print "you finished adding contacts"
        break

# print vseh objects in list: # s for zanko lahko printamo vse kontakte
for contact in all_contacts:
    print 'Kontakti v vasi knjizici so', 'ime: ', contact.firstname, 'priimek: ', contact.lastname, 'email: ', contact.email, 'naslov: ', contact.address




