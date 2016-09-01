"""
brunston 2016
euler 5
"""

def divisible_by(num):
    i = 1
    while num % i == 0:
        if i == 20:
            break
        i = i + 1
    return i == 20

def main():
    num = 2
    while not divisible_by(num):
        num = num + 1
    return num

if __name__ == '__main__':
    print(main())
