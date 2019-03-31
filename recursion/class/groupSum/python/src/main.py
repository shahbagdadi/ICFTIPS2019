"""
Q5::
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target? This is a classic backtracking recursion problem. Once you understand the recursive backtracking strategy in this problem, you can use the same pattern for many problems to search a space of choices. Rather than looking at the whole array, our convention is to consider the part of the array starting at index start and continuing to the end of the array. The caller can specify the whole array simply by passing start as 0. No loops are needed -- the recursive calls progress down the array.


groupSum(0, [2, 4, 8], 10) → true
groupSum(0, [2, 4, 8], 14) → true
groupSum(0, [2, 4, 8], 9) → false
"""

# T - O(?) where ? is ...O(2 power n)
# S - O(?) where ? is ...O(n)

def group_sum(i, arr, target):

    if i == len(arr):
        # print(f"i= {i}, target = {target} base case")
        return target == 0

    if target == 0:
        # print("target == 0")
        return True

    # print(f"i = {i}, target = {target}")
    g_sum = group_sum(i + 1, arr, target - arr[i])

    if not g_sum:
        # print(f"if not g_sum, i={i}, target={target}")
        return group_sum(i + 1, arr, target)

    return g_sum

def main():

    arr = list(map(int, input("enter array elements: ").split()))
    # print(arr)
    target = int(input("enter a target to element to find in group sum array: "))
    # print(target)
    print(group_sum(0, arr, target))

if __name__ == '__main__':
  main()