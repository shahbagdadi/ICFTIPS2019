"""
Given a valid sentence without any spaces between the words and a dictionary of valid English words,
print all possible ways to break the sentence in individual dictionary words. (Recursive solution expected)
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
cream, icecream, man, go, mango}

Input: "ilikesamsungmobile"
Output: i like sam sung mobile
        i like samsung mobile

Input: "ilikeicecreamandmango"
Output: i like ice cream and man go
        i like ice cream and mango
        i like icecream and man go
        i like icecream and mango
"""

# T - O(?) where ? is ...O(n * 2 power n)
# S - O(?) where ? is ...O(n)

word_dict = { 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango', 'and' }


def word_decompose(str_var):
    word_decompose_helper(str_var, 0, [])

def word_decompose_helper(str_var, start, res_list):

    # print("in word decompose function")
    # print(f"start={start} str_v={str_var} lenstr={len(str_var)}")

    if start >= len(str_var):
        print(" ".join(list(map(str, res_list))))
        return

    for end in range(start + 1, len(str_var) +1):

        # print("in for loop")
        # print(f"start={start} end={end} lenstr={len(str_var)}")

        substr = str_var[start:end]
        # print("substr", substr)
        # print(f"start={start} str_var={str_var} lenstr={len(str_var)}")

        if substr in word_dict:
            res_list.append(substr)
            word_decompose_helper(str_var, end, res_list)
            res_list.pop(len(res_list) - 1)

def main():
    print("word decompose for 'ilikesamsungmobile' ")
    word_decompose("ilikesamsungmobile")
    print()
    print("word decompose for 'ilikeicecreamandmango' ")
    word_decompose("ilikeicecreamandmango")

if __name__ == '__main__':
    main()