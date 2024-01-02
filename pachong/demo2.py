# auth:eric.yu
# date: 2023/7/31 16:17
import requests
url='https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1690791958708&loginType=3&uuid=122270672.1628065650725618569159.1628065651.1681797059.1690791791.22&productId=100016486718&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield='
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/115.0.0.0 Safari/537.36'}
r=requests.get(url,headers=headers)
comments=r.json().get('comments')
for c in comments:
    print(c.get('content'))
