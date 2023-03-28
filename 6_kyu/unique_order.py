"""Implement a function unique_in_order which takes as argument a sequence 
and returns a list of items without any elements with the same value next to 
        each other and preserving the original order of elements."""
def unique_in_order(sequence):
   
    # Create a new list
    newList = []

    # Iterate over each item in a sequence
    for item in sequence:

        # Add item to the list each item that is not a replica of the previous one 
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    
    # Return new list
    return newList