"""Implement a function that takes in a string in snake case and converts it to the camel cased one"""
import re
def to_camel_case(text):

    """Split the string at each instance of a hyphen or an underscore"""
    temp = re.split('[-_]+', text)
    
    """Concatenate the string forcing every letter followed by underscore to be capital"""
    return temp[0] + ''.join(map(lambda x: x.title(), temp[1:]))