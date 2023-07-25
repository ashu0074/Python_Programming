import mysql.connector

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = 'localhost', username = 'root', password = '', database = 'hit-db-demo')
            self.mycursor = self.conn.cursor()
        except:
              print("Some error occured. could not connect to database")


        else:
            print("Connected to Database")

    def register(self, name, email, password):
        try:
            # self.mycursor.execute(""" INSERT INTO 'users' ('id','name','email','password') VALUES(NULL, 'Nitish','nitish@gmail.com','1234');""")
            self.mycursor.execute(""" INSERT INTO 'users' ('id','name','email','password') VALUES(NULL, '{}','{}','{}');""".format(name,email,password))
            self.conn.commit()

        except:
            return -1
        else:
            return 1
        
    def search(self, email, password):

        self.mycursor.execute(""" Select * From user where email like "{}" And password like '{}'""".format(email,password))

        data = self.mycursor.fetchall()
        print(data)
# for read query ----> fetchall









# hmesha database se baat kerne ke liye we use "cursor object"--& execute to run any query 