"""
brunston 2016
euler 6
"""

def sum_pow(n, power):
    ret = 0
    for i in range(1,n+1):
        ret = ret + i**power
    return ret

def main():
    return sum_pow(100,2) - sum_pow(100,1)**2

if __name__ == '__main__':
    print(main())
