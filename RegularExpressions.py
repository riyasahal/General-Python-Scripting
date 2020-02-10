#Provides support for regular expressions
import re

exp = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def email_validity(email):
    if (re.search(exp, email)):
        print("The email is valid")
    else:
        print("The email is invalid")

email = input("Enter email ID: ")
email_validity(email)