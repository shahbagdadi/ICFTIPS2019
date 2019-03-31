#!/usr/local/bin/python3

"""
isPalindrome() ?
Given a String return true if it is a palindrome otherwise false.
eg. 1. input "radar" return true.
eg. 2. input "data" return false.
Though there are other ways of solving this problem, a recursive solution is expected here.
"""

# T - O(?) where ? is ...O(n)
# S - O(?) where ? is ...O(n)

def is_palindrome(str_var):
    res_str = is_palindrome_helper(str_var)
    # print("res", res_str)
    # print("str_var", str_var)
    return str_var == res_str


def is_palindrome_helper(str_var):
    # print("strv in rec", str_var)

    if str_var == '':
        return str_var
    else:
        # print("str_var in rec", str_var)
        return is_palindrome_helper(str_var[1:]) + str_var[0]


def main():

    # input for true scenario
    str_var = "radar"

    # input for false scenario
    # str_var = "data"

    if is_palindrome(str_var):
        print("Given a string is palindrome")
    else:
        print("Given a string is not palindrome")


if __name__ == '__main__':
    main()