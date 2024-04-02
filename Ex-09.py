""" 
Problem 9: Remove Duplicates from Sorted Array
Write a Python function to remove the duplicates in-place from a sorted array and return the
length of the new array/list without duplicates.
List = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
"""

def duplicate_remover(input_list):
    check = set()
    ans = []
    for num in input_list:
        if num not in check:
            ans.append(num)
            check.add(num)
    return len(ans)

print(duplicate_remover([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
        