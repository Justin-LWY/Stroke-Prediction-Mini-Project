strongPW = False
PW_LENGTH = 8

users = {"Test":"Test12345", "Jack":"Test12345", "Tom":"Password1"}

print ("User registration:\n")
username = input("input your user name: ")

for user in users:
    if (username == user):
        print("The user exists. Please choose another user name.")
        username = input("input your user name: ")

while strongPW != True:
    password = input('''Input your password:
1.the password has at least one upper case letter
2.the password has at least one lower case letter
3.the password has at least one digit
4.its length is more than 8\n''')

    hasUpper = hasLower = hasDigit =  False

    if len(password) >= PW_LENGTH:
        for letter in password:

            if letter.isupper():
                hasUpper = True
                #print("hasUpper: {}".format(hasUpper))

            elif letter.islower():
                hasLower = True
                #print("hasLower: {}".format(hasLower))

            elif letter.isdigit():
                hasDigit = True
                #print("hasDigit: {}".format(hasDigit))


            #Code for password to have a special character

            # elif not letter.isalnum():
            #     hasSpecial = True
            #     #print("hasSpecial: {}".format(hasSpecial))
            
            else:
                break

    if hasUpper and hasLower and hasDigit == True:
        strongPW = True
        print("Your password is strong enough. User registered.")
        users[username] = password
        print("The users in system\n{}".format(users))
        break

    else:
        print("Your password is weak.Enter a new password") 

print()
