# auth:eric.yu
# date: 2023/7/31 15:32


import requests

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/115.0.0.0 Safari/537.36'}

# r=requests.get('https://www.douban.com/',headers=headers)
#
# print(r)


#构建参数的字典
kw={
    'wd':'python'
}
r=requests.get('http://www.baidu.com/s?',params=kw,headers=headers)
r=requests.post('http://httpbin.org/post',params=kw,headers=headers)
r.encoding='utf-8'
print(r.text)
