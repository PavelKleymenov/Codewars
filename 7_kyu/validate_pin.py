import re
def validate_pin(pin):
    return True if re.fullmatch("\d{4}|\d{6}", pin) else False
    