import random

def generatePassword(num):
    password = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    return "".join(random.sample(password, num))

num = int(input("How long do you want your password to be: "))
print(generatePassword(num))