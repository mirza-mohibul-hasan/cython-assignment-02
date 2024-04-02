""" 
Problem 4: Count Vowels and Consonants
Write a Python function to count the number of vowels and consonants in a given string "Hello
World"
"""


def vowels_onsonants_counter(str):
    str = str.replace(" ", "")
    vowels = 0
    consonant = 0
    for i in range(len (str)):
        if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o'  or str[i] == 'u':
            vowels += 1
        else:
            consonant += 1
    return [vowels, consonant]

print(vowels_onsonants_counter("Hello World"))