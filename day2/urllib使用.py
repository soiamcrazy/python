import urllib.request
#响应类型
response = urllib.request.urlopen('http://www.baidu.com')
print(response)
#状态码
print(response.status)
#响应头
print(response.getheaders())
print(response.getheader('Server'))
#获取网页内容
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))



