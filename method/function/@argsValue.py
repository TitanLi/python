def printArg(*args, **kwargs):
    argsData = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            for d in argsData:
                print(d)
            return func(*args, **kwargs)
        return wrapper

    return decorator

@printArg('Hello','Titan')
def sayHelloPrintArg(arg):
    print(arg)


sayHelloPrintArg('Hello')