#brunston 2016

fib = 0
prev = 1
prev_prev = 1
ret = 0
while fib < 4000000:
    fib = prev + prev_prev
    prev_prev = prev
    prev = fib
    if fib % 2 == 0:
        ret += fib

print(ret)
