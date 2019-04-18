from urllib import request,parse
url = 'http://httpbin.org/post'
headers = {
    'Host': 'httpbin.org',
    'User-Agen':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
dict = {
    'name' : 'HDHD'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
#添加请求头的另一种写法
#req.add_header('User-Agen','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
response = request.urlopen(req)
print(response.read().decode('utf-8'))