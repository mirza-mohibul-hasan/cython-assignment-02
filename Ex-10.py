""" 
Problem 10: Check Anagrams
Write a Python function to check if two given strings ("listen", "silent") are anagrams of each
other (i.e., they contain the same characters but may be in a different order).
"""

def check_anagram(str1, str2):
    #Shortest Way
    # return sorted(str1) == sorted(str2)
    
    #Detailed
    val_str1 = 0
    val_str2 = 0
    for char in str1:
        val_str1 += ord(char)
    for char in str2:
        val_str2 += ord(char)
    return val_str2 == val_str1

print(check_anagram("listen", "silent"))