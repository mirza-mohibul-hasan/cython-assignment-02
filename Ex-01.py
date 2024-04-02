""" 
Problem 1: Fibonacci Sequence
Write a Python function to generate the Fibonacci sequence up to a specified number n. Where n=100
"""
def fibo_seriers(n):
    first  = 0
    second = 1
    print(first)
    print(second)
    while(first+second <= n):
        next = first + second
        first = second
        second = next
        print(next)

fibo_seriers(100)