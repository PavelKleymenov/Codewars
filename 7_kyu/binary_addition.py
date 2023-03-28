"""Implement a function that adds two numbers together 
            and returns their sum in binary. 
    The conversion can be done before, or after the addition."""

def add_binary(a,b):

    """Add to integers together and then use the bin() 
        built - in function to type cast integer into binary.
        Make sure to slice the string so as to remove two 
        leading characters to reach desired format"""
    return bin(a + b)[2:]

# Alternatively, you may implement it as follows:
def add_binary(a,b):

    # The idea remains the same; we just use different tools
    return '{0:b}'.format(a + b)