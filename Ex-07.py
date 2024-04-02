"""
Problem 7: Merge Sorted Lists
Write a Python function to merge two sorted lists into a single sorted list.
List1 = [1, 3, 5]
List2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
"""
def sort_merger(list1, list2):
    return (sorted(list1+ list2))


print(sort_merger(list1 = [1, 3, 5],
list2 = [2, 4, 6]))