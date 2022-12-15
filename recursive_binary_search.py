"""This project searches the given element in the list and gives its index number.
    -this project is done using binary search algorithm and recursive function.
    -list must be in sorted condition."""

# returns index of n in list if present, else returns False
def binary_search(list, low, high, n):

    if high >= low:

        mid = (low+high)//2

        # if element is present at mid itself
        if list[mid] == n:
            return mid

        # if element is smaller than mid
        elif list[mid]> n:
            return binary_search(list, low, mid-1, n)

        # else element is greater than mid
        else:
            return binary_search(list, mid+1, high, n)
    else:
        # element is not present in list
        return False

# test list
list = [1, 2, 5, 11, 35]
n = int(input("Enter element to search: "))

# function call
result = binary_search(list, 0, len(list)-1, n)

if result != False:
    print("Element found at index", str(result))
else:
    print("Element not Found")
