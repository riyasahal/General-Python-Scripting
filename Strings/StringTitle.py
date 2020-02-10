'''
This program demonstrates the usage of Title() method which is used to convert the first character of each word to Uppercase and remaining to Lowercase.
Input: String(From the user)
Returns: New String
'''
def title_convert( your_string ):
    return your_string.title()

your_string = input("Enter a string:")
new_string = title_convert(your_string)
print("Your modified string: %s" % new_string)
