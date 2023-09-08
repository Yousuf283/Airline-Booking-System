import csv
# Imports all the modules that will be used

def write(user, password): 
    row = user,password
    with open('database.csv', 'a', encoding='UTF8', newline='') as file:
        csv.writer(file).writerow(row)
# Function used to write the newly generated Username and Password to the database file using csv module, used in main.py

def read(username, password):
    with open('database.csv', 'r', encoding='UTF8') as file:
        database = csv.reader(file)
        for row in database:
            if row[0] == username and row[1] == password:
                return True
            else:
                pass
    return False
# Function used to read the Username and Password from the database file and check if it is the same as the user given ones using csv module, used in login.py