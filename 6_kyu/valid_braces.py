"""Implement a function that ensures proper utilization of braces inside a string"""
def valid_braces(string):
    
    # Create a list of valid braces 
    brackets = ['()', '{}', '[]']

    # Iterate over entire string, checking if the braces found within are valid
    while any(x in string for x in brackets):
        for bracket in brackets:
            string = string.replace(bracket, '')
    return not string