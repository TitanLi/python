import ast

# JSON
data = {'key':'value'}
print(type(data))
# <type 'dict'>

# String
string = str(data)
print(type(string))
# <type 'str'>

# str to dict
JSON = ast.literal_eval(string)
print(type(JSON))
# <type 'dict'>
