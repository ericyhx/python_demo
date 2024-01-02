# auth:eric.yu
# date: 2023/8/31 16:09


import requests
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/115.0.0.0 Safari/537.36'}
for i in range(1,1000):
    name=""
    if i <10:
        name="000"+str(i)
    elif i<100:
        name ="00"+str(i)
    elif i<1000:
        name ="0"+str(i)
    else:
        name =str(i)
    url='https://hey11.cjkypo.com/202308/25/PRTbAK72Fq3/video/1000k_0X720_64k_25/hls/player'+name+'.ts'
    r=requests.get(url,headers=headers)
    with open('E:\\move_ts\\player'+name+'.ts','wb') as f:
        f.write(r.content)


