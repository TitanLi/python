data = ['a','','b','c','','d']
print(data)

for i in range(data.count('')):
    data.remove('')

print(data)