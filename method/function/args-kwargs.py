# *args是一個list指的是不論個數的輸入參數
# **kwargs是一個dict指的是任何名子的參數
def func(*args, **kwargs):
    for item in args:
        print("I'm args and value is {0}".format(item))
        # I'm args and value is [{'name': 10, 'value': 20}, 1, 2, 3]
        # I'm args and value is 12364
    for key, value in kwargs.items():
        print("I'm kwargs and key and value is {0}={1}".format(key, value))
        # I'm kwargs and key and value is name=1023


func([{
    'name': 10,
    'value': 20
}, 1, 2, 3], 12364)

func(name=1023)