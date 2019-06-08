import types

class ClassA:
    def __init__(self, func):
        self.numberOfCalls = 0
        self.func = func
# 當該方法被呼叫到時的觸發
    def __call__(self, *args, **kwargs):
        self.numberOfCalls += 1
        return self.func(*args, **kwargs)

@ClassA
def add(x, y):
    return x + y


print(add(2, 3))
print(add(4, 5))
print(add.numberOfCalls)