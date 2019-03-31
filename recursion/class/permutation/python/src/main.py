"""
Given a string "abc" , print all permutations of the string.

Example
Input - "abc"
Output
abc
acb
bac
bca
cba
cab
"""

# T - O(?) where ? is ...O(n!)
# S - O(?) where ? is ...O(n)

def perm(str_var):
    return perm_wrapper(str_var, 0)


def swap(str_var, i, j):
    # print(f"swap i={i} j={j}")
    str_var[i], str_var[j] = str_var[j], str_var[i]


def perm_wrapper(str_var, i):

    if i == len(str_var):
        # print("base case= ", "".join(list(map(str, str_var))))
        print("".join(list(map(str, str_var))))
        return

    for j in range(i, len(str_var)):
        # print(f"i={i} j={j} swap  pre-perm")
        swap(str_var, i, j)
        # print("pre-perm swap", "".join(list(map(str, str_var))))
        perm_wrapper(str_var, i + 1)
        # print(f"i={i} j={j} post-perm", "".join(list(map(str, str_var))))
        swap(str_var, i, j)
        # print("post-perm swap", "".join(list(map(str, str_var))))

def main():

    str_var = input("enter a string: ")
    str_var = list(str_var)
    # print(str_var)
    perm(str_var)

if __name__ == '__main__':
  main()