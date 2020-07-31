# put your python code here
def multiply(a, *args):
    m = a
    for x in args:
        m *= x
    return m
