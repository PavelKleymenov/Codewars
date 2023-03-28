"""Implement a function that checks whether or not password is valid, 
        that is if all characters thereof are alphanumeric"""
import re
def alphanumeric(password):

    """You can validate users' input by checking it via the following regular expression.
        Note that underscore is not considered to be an alphanumeric character here.
        Once the regex is written, put in inside of the bool function to avoid if else clause
    """
    return bool(re.search('^[a-zA-Z0-9]+$', password))

# Alternatively, you can reach the same result via well - known string method:
def alphanumeric(password):
    return password.isalnum()