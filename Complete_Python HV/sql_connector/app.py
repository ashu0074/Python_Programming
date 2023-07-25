
""" In this """



import sys

from dbhelper import DBhelper
""" sql connector with python """

class Flipkart:
    def __init__(self):
        # connect to the database
        self.db = DBhelper()          # creating the object of that class

        self.menu()

    def menu(self):

        user_input = input("""Enter your choice:
                            1. Enter 1 to register
                           2. Enter 2 to login 
                           3. Anything else to leave
                           """)
        
        if user_input =='1':
            self.register()
        elif user_input =='2':
            self.login()

        else:
            sys.exit(1000)
        
    
    def register(self):
        name = input("Enter the user_name: ")
        email = input("Enter the email")
        password = input('Enter the password')

        self.db.register(name,email,password)       # paas the value ot dbhelper

        if response:    # true or 1
            print("Registrartion succesfull")

        else:
            print("Registration Failed")

        self.menu()


    def login(self):
        email = input("Enter email")
        password = input("Enter password")

        data = self.db.search(email,password)

        if len(data) ==0:
            print("Incorrect email/password")
        
        else:
            print("hello",data[0][1])    # list with 1st tuple with 1st element the tuple

obj1 = Flipkart()