# 第一個參數類別的實體本身
class Object:
    def func(self, *args, **kwargs):
        print(*args)
        print('do some thing')

var = Object()
var.func(123)