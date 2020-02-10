'''
This program is to check whether a given password is valid or not. We use regular expression to check for the validity.
Input: A password( User Input).
Output: Valid or Invalid password with explanation.
'''
import re

password = input("Enter your password:")
flag =0
char_set = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
while True:
    if len(password) < 8:
        print("The length of your password is less than 8 characters")
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        print("Your password does not contain any uppercase characters")
        flag = -1
        break
    elif not re.search("[a-z]", password):
        print("Your password does not contain any lowercase characters")
        flag = -1
        break
    elif not re.search("\d", password):
        print("Your password does not contain any numbers")
        flag = -1
        break
    elif not char_set.search(password):
        print("Your password does not contain any special characters")
        flag = -1
        break
    else:
        print("Valid password")
        break

if flag == -1:
    print("Invalid Password")
