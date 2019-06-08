import types

class ClassB:
    def __init__(self, func):
        self.numberOfCalls = 0
        self.func = func
# 當該方法被呼叫到時的觸發
    def __call__(self, *args, **kwargs):
        self.numberOfCalls += 1
        return self.func(*args, **kwargs)
# 確保綁定方法對象能被正確的創建
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

class ClassA:
    @ClassB
    def test(self, x):
        print(self, x)

s = ClassA()
s.test(1)
s.test(2)
s.test(3)
print(ClassA.test.numberOfCalls)