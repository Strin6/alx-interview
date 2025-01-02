#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """Minimum Operations needed to get n H characters"""
    
    if n < 1:
        return 0
    
    operations = 0
    current_length = 1
    
    while current_length < n:
        if n % current_length == 0:
            operations += 1
            current_length *= 2
        else:
            operations += 1
            current_length += 1
    
    return operations