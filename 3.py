"""
brunston 2016
Euler 3
"""

from math import ceil, sqrt

#make is_prime only search to square root
#make main() begin with low values that % = 0, then divide n by that value to get the corresponding
#   big value and test *that* value for prime-ness.
def is_prime(n):
    if n == 2:
        return True
    else:
        for i in range(2,ceil(sqrt(n))):    
            #print("now dividing "+str(n)+" by "+str(i))
            if (n % i) == 0:
                return False
        return True

def main():

    n = 600851475143
    limit_of_search = ceil(sqrt(n))

    highest_prime_factor = 2
    for i in range(n-1,limit_of_search,-1):
        if n % i == 0:
            print("found candidate"+str(i))
            if (is_prime(i) == True):
                highest_prime_factor = i
                break
    
    print(highest_prime_factor)
    return highest_prime_factor

if __name__ == '__main__':
    main()
