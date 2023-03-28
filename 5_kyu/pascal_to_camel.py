"""Implement a program that convert input in Pascal case to the Camel cased one"""
import re
def to_underscore(string):

    """First off, you need to split input at each instance of a capital letter, 
                    and store the result in a variable"""
    temp = re.split('(?=[A-Z])', str(string))

    """Having done that, you need to concatenate the part to the left of the capital 
            letter and then forcing capital letter to become lowercased one, 
            as well as separating different parts by an underscore """
    return temp[0] + '_'.join(map(lambda x: x.lower(), temp[1:]))

