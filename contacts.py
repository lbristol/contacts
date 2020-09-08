import sqlite3
import re

conn = sqlite3.connect('contacts.db')

c = conn.cursor()

class main:
    def __init__(self):
        firstcheck = 0
        lastcheck = 0
        phonecheck = 0
        emailcheck = 0
        checks = 0
        while checks < 4:
            checks = firstcheck + lastcheck + phonecheck + emailcheck
            if firstcheck == 0:
                self.first = input("Enter contact's first name: ")
                if self.first.isalpha():
                    firstcheck = 1
                else:
                    print("Looks like you may have made a typo. Try again.")
                    continue

            if lastcheck == 0:
                self.last = input("Enter contact's last name: ")
                if self.last.isalpha():
                    lastcheck = 1
                else:
                    print("Looks like you may have made a typo. Try again.")
                    continue

            if phonecheck == 0:
                self.phone = input("Enter contact's phone #: ")
                self.phone = re.sub("[()-]", "", self.phone)
                if self.phone.isnumeric():
                    phonecheck = 1
                else:
                    print("Looks like you may have made a typo. Try again.")
                    continue

            if emailcheck == 0:
                self.email = input("Enter contact's email address: ")
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                if re.search(regex, self.email) or self.email == "":
                    emailcheck = 1
                else:
                    print("Looks like you may have made a typo. Try again.")
                continue

        lenc = c.execute("SELECT * FROM contacts")
        id = str(len(lenc.fetchall()) + 1)

        try:
            c.execute("INSERT INTO contacts VALUES ('" + id + "', '" + self.first + "', '" + self.last + "', '" + self.email + "', '" + self.phone + "');")
        except:
            print("Looks like that's not a unique entry.")
        conn.commit()


while True:
    x = input("Would you like to add another entry to the contact list? y/n ")
    if x.isalpha:
        if x.upper() == "N":
            break
        elif x.upper() == "Y":
            go = main()
        else:
            print("Looks like you made a typo.")
            continue
    else:
        print("Looks like you made a typo.")
        continue

conn.close()
