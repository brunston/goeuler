"""
brunston 2016
eueler 7
"""
from math import floor, sqrt
def prime(n):
    """returns nth prime"""
    prime_list = [2]
    iterator = 1
    while iterator <= 10001:
        if is_prime_pl(iterator, primelist):
            

def is_prime_pl(num, primelist):
    for prime in primelist:
        if num % prime == 0:
            return False

    return True

def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3,floor(sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True

def main():
    return prime(10001)
if __name__ == "__main__":
    print(main())
