import json
import ast

# JSON
data = {"keyData":"value"}
print(type(data))
# <type 'dict'>

# dumps (str)
dumpsData = json.dumps(data)
print(type(dumpsData))
# <type 'str'>
print(dumpsData)

# loads (dict)
loadsData = json.loads(json.dumps(data))
print(type(loadsData))
# <type 'str'>
print(loadsData['keyData'])
# value

# str to dict
astData = ast.literal_eval(dumpsData)
print(type(astData))
# <type 'dict'>