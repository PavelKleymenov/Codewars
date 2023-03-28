"""Find a unique number within an array"""
def find_uniq(arr):

    # Filter out duplicates by forcing an array to become a set
    a, b = set(arr)

    # Return the number if it's not repeated more than once
    return a if arr.count(a) == 1 else b


# Alternarively ...
def find_uniq(arr):

    # Sort the array first
    arr.sort()

    # Unique number is the 0 - indexed element if no duplicates do follow it
    if(arr[0] < arr[len(arr) - 1] and arr[0] < arr[len(arr) - 2]):
        n = arr[0]

    # Else it has to be somewhere in the array    
    else:
        n = arr[len(arr) - 1]
    return n

