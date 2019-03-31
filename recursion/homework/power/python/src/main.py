"""
Q1:
Implement a power function to raise a double to an int power, including negative powers.
e.g. pow(double d, int p) should give 'd' raised to power 'p'.
Of course, please don't use in-built methods like pow(). Idea is to implement that using
recursion.

Solution: http://stackoverflow.com/questions/101439/the-most-efficient-way-to-implement-aninteger-
based-power-function-powint-int
Suggested time: 10 minutes to do a brute-force and 15 with a trick that optimizes it.
"""

# T - O(?) where ? is ...O(n)
# S - O(?) where ? is ...O(n)

def power_of_n_method1(base, n):

    # base case
    if n == 0:
        return 1

    return base * power_of_n_method1(base, n - 1) if n > 0 else 1/base * power_of_n_method1(base, n + 1)


def power_of_n_method2(base, n):

    # if n is -ve number
    if n < 0:
        base = 1 / base
        n = - n

    # base case
    if n == 0:
        return 1

    return base * power_of_n_method2(base, n - 1)

def main():
    print(power_of_n_method1(2.0, -4))
    print(power_of_n_method2(2.0, -4))

if __name__ == '__main__':
  main()