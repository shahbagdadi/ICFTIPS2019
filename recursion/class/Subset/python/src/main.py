"""
Q2:
Problem:
Print out all the subsets of a set.
E.g.
{x,y} ==> {{}, {x}, {y}, {x,y}} [Remember, that we are working with sets, so {y,x} is not
different from {x,y}, and {x,x} is not a valid subset, unless the input also has two x's]
{1, 2, 3} ==> {{}, {1}, {2}, {3}, {1,2}, {1,3}, {2, 3}, {1,2,3}}
Input: Set, as an array
Output: Subsets in any order.
This problem does not have pre-defined test-cases, in order to give you the flexibility of doing
outputs in any order, and in any print format.
Solutions:
http://stackoverflow.com/questions/728972/finding-all-the-subsets-of-a-set OR
http://stackoverflow.com/questions/4640034/calculating-all-of-the-subsets-of-a-set-of-numbers
(Suggested time: 20 minutes)

from repository:
Given a set of distinct integers, nums, return all possible subsets (the power set).



Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]



"""

# T - O(?) where ? is ...O(2 power n)
# S - O(?) where ? is ...O(n)

def power_set(arr):

    res_arr = [None] * len(arr)
    # read 0 and write 0
    return power_set_helper(arr, 0, res_arr, 0, [])



def power_set_helper(arr, read, res_arr, write, res_list):

    if read >= len(arr):
        # print("read = {} write = {} read>= len base case".format(read, write))

        print("{", end=" ")

        for i in range(write):
            if not (res_arr[i] is None):
                print(res_arr[i], end=" ")

        print("}", end=' ')

        return   #  important step

    #print("read = {} write = {} read < len dont' select case".format(read, write))
    power_set_helper(arr, read+1, res_arr, write, res_list)   # dont't select

    # print("read = {} write = {} res_arr[{}] = arr[{}] = {} assignment case".format(read, write, write, read, arr[read]))
    res_arr[write] = arr[read]
    #print("read = {} write = {} write <len and read < len select case".format(read, write))
    power_set_helper(arr, read + 1, res_arr, write + 1, res_list) # select

def main():
    arr = input("enter array elements: ")
    arr = list(arr)
    #print(arr)
    power_set(arr)

if __name__ == '__main__':
  main()