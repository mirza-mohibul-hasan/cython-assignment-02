""" 
Problem 3: Find the Missing Number
Given a list of n-1 integers from 1 to n, find the missing number in the list.
List = [1, 2, 4, 6, 3, 7, 8] # Output: 5
"""

def missing_finder(input_list):
    n = len(input_list)+1
    sum_list  = sum(input_list)
    sum_total = int(n * (n+1)/2)
    
    return sum_total - sum_list

print(missing_finder([1, 2, 4, 6, 3, 7, 8]))