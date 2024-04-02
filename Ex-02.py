""" 
Problem 2: Reverse Words in a String
Write a Python function to reverse the order of words in a given string - "Hello World"
"""

#Approch 01
def word_order_reverser(str):
    word_list_reverse  = list(str.split(" "))[::-1]
    word_reverse = " ".join(word_list_reverse)
    return word_reverse
    
print(word_order_reverser("Hello World"))

#Approch 02
def word_order_reverser_A2(str):
    word_list_reverse  = list(str.split(" "))
    word_list_reverse.reverse()
    word_reverse = ""
    for i in range (len(word_list_reverse)):
        if(i == len(word_list_reverse)-1):
            word_reverse += word_list_reverse[i]
        else:
            word_reverse += word_list_reverse[i] + " "
        
    return word_reverse
print(word_order_reverser_A2("Hello World"))