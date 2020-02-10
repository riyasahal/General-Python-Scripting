# Recursive Binary Search

def BinarySearch(Arr, left, right, element):
    # Check the array, shouldnt be empty.
    if right >= 1:
        mid = int((left + right) / 2)
        # If element is present in the middle, return the pos
        if Arr[mid] == element:
            return mid
        # If element is smaller than the middle element, assign the middle place as the right most limit
        elif Arr[mid] > element:
            return BinarySearch(Arr, left, mid - 1, element)
        # Else the element will be present in the right side of the array, assign the lower range to point middle.
        else:
            return BinarySearch(Arr, mid + 1, right, element)
    else:
        return -1



list_of_elements = input("Enter a list of numbers:")
Arr = list_of_elements.split()
element = int()
element= input("Enter element to be searched:")
result = BinarySearch(Arr, 0, len(Arr) - 1, element)

if result != -1:
    print(" Element is at index %d" % result)
else:
    print("Element is not present in the array")



