"""
brunston 2016
euler 4
"""

from math import ceil

def is_palindrome(num):
    """
    defines a number if it's a palindrome
    """
    num_str = str(num)
    for i in range(0,ceil(len(num_str))):
        if not int(num_str[i]) == int(num_str[-i-1]):
            return False
    return True

def main():
    largest_palindrome = 0
    for i in range(1000,100, -1):
        for j in range(1000,100, -1):
            if is_palindrome(i*j) and i*j > largest_palindrome:
                largest_palindrome = i*j
    print(largest_palindrome)

if __name__ == '__main__':
    main()
