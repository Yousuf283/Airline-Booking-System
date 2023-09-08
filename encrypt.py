import hashlib
# Imports all the modules that will be used

def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()
# Function used to encrypt a given password using hashlib module, used in login.py
