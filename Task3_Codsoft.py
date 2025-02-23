import random
def genpass(length):
    char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    passwrd=""
    for i in range(length):
        passwrd+=random.choice(char)
    return passwrd
length = int(input("Enter the length of the password:"))
passwrd = genpass(length)
print("The generated password is :",passwrd)