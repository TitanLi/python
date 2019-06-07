def printHello(func):
    def hello():
        print('Hello')
        return func()
    return hello

@printHello
def printWorld():
    print('World')

printWorld()

print(">>>>>>>>>>>>下方功能與上方功能一樣>>>>>>>>>>>>>>>")

def printHello1(func):
    print('Hello')
    return func()

def printWorld1():
    print('World')
printHello1(printWorld1)