""" 
Problem 8: Find Duplicate Elements
Write a Python function to find all duplicate elements in a list and return them in a new list.
List = [1, 2, 3, 2, 4, 5, 4, 6] 
"""
def duplicates_finder(input_list):
    check = {}
    ans = []
    for num in input_list:
        if num in check:
            check[num] += 1
        else:
            check[num] = 1
    for num in check:
        if check[num] > 1:
            ans.append(num)
    return ans

print(duplicates_finder([1, 2, 3, 2, 4, 5, 4, 6] ))