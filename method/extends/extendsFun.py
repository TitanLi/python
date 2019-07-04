class A(object):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = kwargs['number']
 
    def helloA(self):
        return self.number
 
class B(object):
 
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.message = kwargs['message']
 
    def helloB(self):
        return self.message
 
class C(A,B):
 
    def __init__(self, *args, **kwargs):
        # Notice: only one call to super... due to mro
        super().__init__(*args, **kwargs)
 
    def helloC(self):
        print("Calling A: ", self.helloA())
        print("Calling B: ", self.helloB())  
 
def main():
    c = C(number=42, message="Joe")
    c.helloC()

# 解
# Calling A:  42
# Calling B:  Joe
 
if __name__ == '__main__':
    main()