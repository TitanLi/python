# 類別方法裝飾器第一個參數就是綁訂在一個類別物件的實體cls
# 這時候不管產生多少類別物件的實體
# 他所用到的類別方法所綁定的類別物件實體都會是同一個
class Object:
    @classmethod
    def func(cls, *args, **kwargs):
        print('do some thing')

var = Object()
var.func()