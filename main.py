import string
print("The password length must be at least 6, and no more than 12 characters")
password = input("Enter your password:")
length = len(password)
upperChars = 0
lowerChars = 0
specialChars = 0
digits = 0
score = 0
weak = 'weak'
med = 'medium'
strong = 'strong'

with open('common.txt', 'r') as file:
    common = file.read().splitlines()

if password in common:
    print("Password was found in a common list. Weak password!")
    exit()

if length > 12:
    print('Password is too long!')
    exit()
    

if length < 6:
    print('Password is too short!')
    exit()
    

else:
    for i in range(0, length):
        if(password[i].isupper()):
            upperChars += 1
        elif(password[i].islower()):
            lowerChars += 1
        elif(password[i].isdigit()):
            digits += 1
        else:
            specialChars += 1

if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if (length >= 10):
            print("The strength of password is strong.\n")
        else:
            print("The strength of password is medium.\n")
else:
    if (upperChars == 0):
        print("Password must contain at least one uppercase character!\n")
    if (lowerChars == 0):
        print("Password must contain at least one lowercase character!\n")
    if (specialChars == 0):
        print("Password must contain at least one special character!\n")
    if (digits == 0):
        print("Password must contain at least one digit!\n")

        


