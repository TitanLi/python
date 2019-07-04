import requests

data = open('./free5gc.yaml', 'rb').read()
res = requests.post(url='http://10.0.1.13:30007/run',
                    data=data,
                    headers={
                                'xos-username': 'admin@opencord.org',
                                'xos-password': 'letmein'
                            }
                    )
print(res)