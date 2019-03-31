#!/usr/local/bin/python3

"""
Partition Equal Subset Sum
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1: Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].



Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


# T - O(?) where ? is ...O(2 power n)
# S - O(?) where ? is ...O(n)

def equal_part_subset(arr):

    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    target = sum / 2

    return equal_part_subset_helper(0, arr, target)

def equal_part_subset_helper(i, arr, target):

    if i == len(arr):
        # print(f"i= {i}, target = {target} base case")
        return target == 0

    if target == 0:
        # print("target == 0")
        return True

    # print(f"i = {i}, target = {target}")
    equal_part_sum = equal_part_subset_helper(i + 1, arr, target - arr[i])

    if not equal_part_sum:
        # print(f"if not equal_part_sum, i={i}, target={target}")
        return equal_part_subset_helper(i + 1, arr, target)

    return equal_part_sum

def main():

    arr = list(map(int, input("enter array elements: ").split()))
    # print(arr)

    print(equal_part_subset(arr))

if __name__ == '__main__':
  main()