import os
import random
import data
import encrypt as e
# Imports all the modules that will be used

def gen_user():
    first = input("What is your First name?: ")
    last = input("What is your Last name?: ")
    first = first.replace(' ', '')
    last = last.replace(' ', '')
    username = ""
    username += first[0]
    username += first[random.randint(1, len(first)-1)]
    username += last[random.randint(1, len(last)-1)]
    username += last[0]
    username = username.lower()

    return username
# Generates a Username for the user using their first name and last name and the random module
# First it asks the user for their first and last names
# Second it gets rid of any spaces in the names
# Third it takes the first letter and a random letter of the first name and adds it to the empty variable "username" respectively
# Fourth it takes a random letter and the first letter of the second name and adds to the variable "username" respectively
# Fifth it converts all the letters in the variable "username" into lowercase
# Sixth it returns the user their new Username

def gen_pass(): 
    list = []

    for i in range(3):
        temp_list = []
        temp_list.append(random.randint(0,1))
        temp_list.append(random.randint(0,25))
        list.append(temp_list)

    list.append(random.randint(0,9))

    for i in range(3):
        temp_list = []
        temp_list.append(random.randint(0,1))
        temp_list.append(random.randint(0,25))
        list.append(temp_list)

    special_chars = '”!#%'

    list.append(special_chars[random.randint(0,3)])

    password = ''

    for i in range(3):
        if not list[i][0]:
            password += chr(list[i][1] + 97)
        else:
            password += chr(list[i][1] + 65)

    password += str(list[3])

    for i in range(4,7):
        if not list[i][0]:
            password += chr(list[i][1] + 97)
        else:
            password += chr(list[i][1] + 65)

    password += list[7]

    return password
# Generates a password for the user using a range of numbers and the random module
# First it does 3 iterations of generating and appending a random integer in the ranges 0-1 and 0-25 in a temp list then adds the temp list it to the main list
# Second it adds a single random integer in the range 0-9 to the list
# Third it does the first step again
# Fourth it adds a random special character to the list
# Fifth it iterates through the first 3 items in the list which would be the 3 added lists from the first step and generates a character where the first item represents upper/lower case 
# and the second represents the the position of the character in the alphabet then adds that character to the empty variable password
# Sixth it adds the 4th item in the list as a string to the variable password
# Seventh it does the fifth step again for items 5-7
# Eighth it adds the 8th item in the list as a string to the variable password
# Ninth it returns the user their new Password

def validate(username, password):
    password = e.encrypt(password)
    if data.read(username, password):
        return True
    else:
        return False
# Validates whether a Username and Password given by a user is correct when logging in using the data and the encrypt modules
# First it encrypts the password 
# Second it checks if the username and the now encrypted password is in the database
# If it is, returns True
# If its not, returns False