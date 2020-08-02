def morning(func):
    def decorator(name):
        func(name)
        print('Good morning,', name)
    return decorator
