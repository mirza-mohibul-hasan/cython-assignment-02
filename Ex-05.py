""" 
Problem 5: Palindrome Check
Write a Python function to check if a given string is a palindrome or not.
String = "A man, a plan, a canal, Panama" 
"""


def palindrome_check(str):
    # str = str.replace(" ","").replace(",","").lower()
    str = ''.join(char for char in str if char.isalnum()).lower()
    str_rev = str[::-1]
    return str == str_rev
    
print(palindrome_check("A man, a plan, a canal, Panama"))