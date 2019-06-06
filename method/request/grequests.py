# async request
import grequests

urls = [
        'http://10.0.1.37:5000/?network=',
        'http://10.0.1.21:5000/?network=',
        'http://10.0.1.23:5000/?network=',
        'http://10.0.1.22:5000/?network='
        ]
results = grequests.map((grequests.get(u) for u in urls), size=4)
print(results)