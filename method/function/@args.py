def printHello(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        return func(*args, **kwargs)
    return wrapper

@printHello
def printSingle(arg):
    print(arg)

@printHello
def printDouble(arg1, arg2):
    print(arg1)
    print(arg2)

printSingle('World')
printDouble('Kitty', 'Danny')
