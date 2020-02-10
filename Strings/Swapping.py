'''
This program swaps commas and dots in a string using maketrans and translate function, also using the replace method.

Input: String with commas and dots (User Input)
Output: Swapped String

'''

#This method demonstrates the use of maketrans and translate() method
def replace_char(string_2):
    transition_string =  string_2.maketrans(".,",",.")
    string_2 = string_2.translate(transition_string)
    print("Your new string is:" + string_2)


#This method demonstrates the use of replace() method
def char_replace(string_1):
    string_1 = string_1.replace('.', '&')
    string_1 = string_1.replace(',', '.')
    string_1 = string_1.replace('&', ',')
    print("Your new string is:%s" % string_1)

string = input("Enter your string:")
replace_char(string)
string_1 = input("Enter your string:")
char_replace(string_1)
