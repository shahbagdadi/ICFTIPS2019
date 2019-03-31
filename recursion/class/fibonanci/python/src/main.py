"""
The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the start of the sequence.

fibonacci(0) → 0
fibonacci(1) → 1
fibonacci(2) → 1
"""

# T - O(?) where ? is ...O(2 power n)
# S - O(?) where ? is ...O(n)

def fib(n):

    #Base case
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def main():
    n = int(input("enter n: "))
    print(fib(n))

if __name__ == '__main__':
  main()