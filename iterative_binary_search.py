"""This project searches the given element in the list and gives its index number.
    -this project is done using binary search algorithm and itarative.
    -list must be in sorted condition."""

# returns index of n in list if present, else returns False
def binary_search(list, n):

    low = 0
    high = len(list)-1

    while low <= high:

        mid = (high + low) // 2

        # if element is greater than mid
        if list[mid] < n:
            low = mid + 1
 
        # if element is smaller than mid
        elif list[mid] > n:
            high = mid - 1
 
        # else element is present at mid
        else:
            return mid
    
    else:
        # element is not present in list
        return False

# test list
list = [1, 2, 5, 11, 35]
n = int(input("Enter element to search: "))

# function call
result = binary_search(list, n)

if result != False:
    print("Element found at index", str(result))
else:
    print("Element not Found")