class Contacts():
    def __init__(self, contactName, phoneNumber):
        self.name = contactName
        self.number = phoneNumber
    
    # display the details of the object
    def display_details(self):
        print(f"\nName: {self.name}\nPhone Number: {self.number}")
        print('-'*30)
        pass
    
    # returns the name of the object
    def getName(self):
        return self.name

    # returns the number of the object
    def getNumber(self):
        return self.number
        