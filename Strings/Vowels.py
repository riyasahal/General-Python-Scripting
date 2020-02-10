'''
This program counts and displays the vowels in a string using two different methods.
Input: String(User Input)
Output: Number & List of vowels in the string
'''

def vowel_count( string, vowel):
    vowel_num = [each for each in string if each in vowel]
    print("Number of vowels in your string:%d"%len(vowel_num))
    print("The list of vowels in your string:%s"%vowel_num)

def count_vowel( string, vowel):
    count = {}.fromkeys(vowel,0)
    for each in string:
        if each in count:
            count[each] += 1
    print("Number of vowels in your string:", count)

vowel="AaEeIiOoUu"
string = raw_input("Enter your string:")
input_choice = int(input("Which method would you prefer? \n1. For loop\n2. Dictionary\nEnter your choice(1-2):"))
if input_choice == 1:
    vowel_count(string,vowel)
elif input_choice == 2:
    count_vowel(string, vowel)
else:
    print("Wrong Input")

