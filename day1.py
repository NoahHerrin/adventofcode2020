""" Day 1, advent of code

Given a file containing an integer on each line. Find the combination
of integers whose sum is equal to 2020. Then multiply those two integers
integers together. 

Strategies
    Brute Force
        O(n^2): for each number in the list loop through the list
        and see if it's sum with another value equals zero. 
    Improved Brute force
    Ex. [a,b,c,d,e]
    check a + b
    check a + c
    check a + d
    check a + e
    check b + c
    check b + d
    check d + e
    check c + d
    check c + e
    check d + e
    

"""
import sys

EXPENSE_REPORT_PATH = './res/day1_input.txt'
TARGET = 2020

def load_expense_report(file_name):
    """creates a list of integers 
    where each entry was an integer on each line
    in the provided file.
    """
    entries = []
    with open(file_name, mode='r') as f:
        for line in f.readlines():
            entries.append(int(line.strip()))
    return entries

def find_pair_with_sum(target, nums):
    n = len(expenses)
    
    for i in range(n):
        for j in range(i, n):
            if expenses[i] + expenses[j] == TARGET:
                return expenses[i], expenses[j]
    return -1, -1

if __name__ == '__main__':

    expenses = load_expense_report(EXPENSE_REPORT_PATH)
    num1, num2 = find_pair_with_sum(TARGET, expenses)

    # determine whether solution was found
    if num1 == -1:
        print(f'Solution was not found.')
    else:
        print(f'Solution is {num1} + {num2} = 2020')
        print(f'Their product is {num1 * num2}')