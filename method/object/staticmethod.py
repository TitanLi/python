# 靜態方法裝飾器上沒有給予類別的實體
class Object:
    @staticmethod
    def func(*args, **kwargs):
        print('do some thing')

var = Object()
var.func()