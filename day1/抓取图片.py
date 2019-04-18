import requests
response = requests.get("https://i0.hdslb.com/bfs/sycp/creative_img/201904/94e03983c0969e85c4ea007723562c09.jpg")
print(response.content)
with open('C:/Users/15093/Desktop/python学习记录/图片/1.jpg','wb') as f:
    f.write(response.content)
    f.close()