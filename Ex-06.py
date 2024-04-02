"""
Problem 6: Count Occurrences
Write a Python function to count the occurrences of each element in a list and return a dictionary
with the counts.
List = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
"""

def count_occurence(input_list):
    ans = {}
    for num in input_list:
        if num in ans:
            ans[num] += 1
        else:
            ans[num] = 1
    return ans
print(count_occurence([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))