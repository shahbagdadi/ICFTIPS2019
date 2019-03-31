#!/usr/local/bin/python3

"""
Q3:
Input: 10?
Output: 101, 100
i.e. ? behaves like a wild-card. There are two possibilities for 10?, when that ? is replaced with
either 0 or 1.
Input: 1?0?
Output: 1000, 1001, 1100, 1101
Please write a program that takes given strings as input and produces the suggested output.
Suggested time: 20 minutes.
"""

# T - O(?) where ? is ...O(2 power n)
# S - O(?) where ? is ...O(n)

def print_wildcard_string(str_var):

    return print_wildcard_string_helper(str_var, 0)


def print_wildcard_string_helper(str_var, i):

    if i == len(str_var):
        print("".join(list(map(str, str_var))))
        # print(str_var)
        return

    #print(str_v[i])

    if str_var[i] == '?':
        str_var[i] = '0'
        print_wildcard_string_helper(str_var, i+1)

        str_var[i] = '1'
        print_wildcard_string_helper(str_var, i+1)
        str_var[i] = '?'   # back tracking
    else:
        print_wildcard_string_helper(str_var, i + 1)


def main():
    str_var = input("enter a string in the format of binary numbers along with wild card ex: 10?  or 1?0? :  ")
    str_var = list(str_var)
    print_wildcard_string(str_var)


if __name__ == '__main__':
    main()