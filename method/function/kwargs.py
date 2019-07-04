def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(foo='bar', hello='world')

# 解
# {'foo': 'bar', 'hello': 'world'}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def print_data(latitude=None, longitude=None):
    print(latitude, longitude)

data = {'latitude': 0.00, 'longitude': 1.00}
print_data(**data)

# 解
# 0.0 1.0

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def print_args_kwargs(lat=None, long=None, **kwargs):
    print(lat, long, kwargs)
print_args_kwargs(1, 2, data='other')

# 解
# 1 2 {'data': 'other'}