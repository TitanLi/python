def printArg(*args, **kwargs):
    kwargsData = kwargs
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(kwargsData['keyName'])
            return func(*args, **kwargs)
        return wrapper

    return decorator

@printArg(keyName='Hello')
def sayHelloWorldPrintArg(arg):
    print(arg)


sayHelloWorldPrintArg('World')