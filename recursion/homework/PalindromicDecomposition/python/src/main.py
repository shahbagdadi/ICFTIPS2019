"""
Q7: Palindromic Decomposition
A “Palindromic Decomposition” of string S, is a decomposition of the string into substrings,
such that all those substrings are valid palindromes. A single character is considered a valid
palindrome for this problem. Print out all possible palindromic decompositions of a given
string.
e.g.
Input: abracadabra
Output:
a|b|r|a|c|a|d|a|b|r|a|
a|b|r|a|c|ada|b|r|a|
a|b|r|aca|d|a|b|r|a|
Solution: http://www.programcreek.com/2013/03/leetcode-palindrome-partitioning-java/
"""

# T - O(?) where ? is ...O(n * 2 power n)
# S - O(?) where ? is ...O(n)

def is_palindrome(str_v):
    res = is_palindrome_helper(str_v)
    # print("res", res)
    # print("str_v", str_v)
    return str_v == res


def is_palindrome_helper(str_v):
    # print("strv in rec", str_v)

    if str_v == '':
        return str_v
    else:
        # print("strv in rec", str_v)
        return is_palindrome_helper(str_v[1:]) + str_v[0]

def palindromic_decompose(str_var):
    palindromic_decompose_helper(str_var, 0, [])

def palindromic_decompose_helper(str_var, start, res_list):

    #print("in word decompose function")
    #print(f"start={start} str_v={str_var} lenstr={len(str_var)}")

    if start >= len(str_var):
        print("|".join(list(map(str, res_list))))
        return

    for end in range(start + 1, len(str_var) +1):

        #print("in for loop")
        #print(f"start={start} end={end} lenstr={len(str_var)}")

        substr = str_var[start:end]
        # print("substr", substr)
        # print(f"start={start} str_var={str_var} lenstr={len(str_var)}")

        if (is_palindrome(substr)):
            res_list.append(substr)
            palindromic_decompose_helper(str_var, end, res_list)
            res_list.pop(len(res_list) - 1)


def main():

    palindromic_decompose("abracadabra")


if __name__ == '__main__':
    main()
