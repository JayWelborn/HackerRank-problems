"""Project Euler Problem #2.

This code snippet finds the sum of all even Fibonacci numbers below
given number (n).
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    even_sum = 0
    a = 0
    b = 1
    fib = 0
    while fib < n:
        if fib % 2 == 0:
            even_sum += fib
        fib = a + b
        a = b
        b = fib

    print(even_sum)
