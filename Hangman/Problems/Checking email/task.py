def check_email(string):
    if ' ' in string:
        return False
    if not string.count('@') == 1:
        return False
    if not string.count('.', string.index('@') + 2) == 1:
        return False
    return True
