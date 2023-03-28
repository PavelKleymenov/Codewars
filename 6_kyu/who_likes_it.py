"""Implement a function which takes an array containing the names of people that like an item."""
def likes(names):

    """Make use of the match - case, ensuring proper output based upon 
                    the number of arguments passed in"""
    n = len(names)
    match n:
        case 0:
            return 'no one likes this'
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} like this"
        case 3:
            return  f"{names[0]}, {names[1]} and {names[2]} like this"
        case _:
            return f"{names[0]}, {names[1]} and {n-2} others like this"
        
# You may also do something along what follows:
def likes(names):
    n = len(names)
    match n:
        case 0:
            return 'no one likes this'
        case 1: 
            return '{} likes this'.format(names[0])
        case 2:
            return '{} and {} like this'.format(names[0], names[1])
        case 3:
            return '{}, {} and {} like this'.format(names[0],names[1], names[2])
        case _:
            return '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)