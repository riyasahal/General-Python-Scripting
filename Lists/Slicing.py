'''
This program implements the reversal of an list in groups of the given size.
Input:
1. List
2. Size of the group
Output: List meeting the required condition
'''

def reversal(arr, k):
    start = 0
    array = []
    while start < len(arr):
        if len(arr[start:]) < k:
            array = array + list(reversed(arr[start:]))
            break

        array = array + list(reversed(arr[start:start+k]))
        start = start + k
    print("Your new array:", array)

print("Enter your array elements:")
arr = [int(x) for x in input().split()]
k = int(input("Enter the group size for your array"))
reversal(arr,k)
