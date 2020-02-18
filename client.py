import requests
import datetime
import os

url = 'http://127.0.0.1:5000/data'
url2 = 'http://127.0.0.1:5000/data2'


now = datetime.datetime.now()

params = {'req_lat': '37.557594', 'req_lng': '127.033456', 'req_t1' : '10', 'req_t2' : '10', 'req_h' : '20', 'req_date' : now.strftime('%Y-%m-%d'), 'req_time' : now.strftime('%H:%M:%S')}
response = requests.get(url, params=params)

print("get : ", response)


'''
files = {
    'file': (
        open('test3.jpg', 'rb'), 
        'application/octet-stream'
    )
}
'''

files = {'file': open('test3.jpg', 'rb')}

requests.post(url2, files=files)

print("post : ", requests.post(url, files=files))