# NUMBER 1

# This function determines if a number is prime or not
def prime(n):
    count = 0
    if n == 0:
        return False;
    for i in range(1, n + 1):
        if (n % i) == 0:
            count += 1
    if count == 2:
        return True
    return False

# This function returns a list of primes between 0 and n (inclusive)
def primeFrom0ToN(n):
    lst = []
    if (n < 2):
        return lst
    for i in range(1, n + 1):
        if prime(i):
            lst.append(i)
    return lst

# This function prints a list of primes between 0 and n (inclusive)
def printListPrime(n):
    print(primeFrom0ToN(n))

#######################################################################

# NUMBER 2

# This function returns the nth fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

# This function prints the nth fibonacci number
def printFib(n):
    print(fib(n))

#######################################################################

# NUMBER 3

# This function prints the number in the summation order
def numTriangle(n):
    lst = []
    while (n > 0):
        lst.append(n % 10)
        n = n // 10
    i = 0
    while (i < len(lst)):
        loc = len(lst) - i - 1
        print(lst[loc] * (10 ** loc))
        i += 1