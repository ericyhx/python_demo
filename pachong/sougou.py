# auth:eric.yu
# date: 2023/7/31 16:39
import requests
url='https://webfs.tx.kugou.com/202307311635/4664a9adfa8c8039a0cd42f64383b19f/v2/60ea89a9d0e2e33779127ea2b2e7d51a/KGTX/CLTX001/60ea89a9d0e2e33779127ea2b2e7d51a.mp3'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/115.0.0.0 Safari/537.36'}
# r=requests.get(url,headers=headers)
# with open('zzz.mp3','wb') as f:
#     f.write(r.content)


url='https://www.kugou.com/yy/html/rank.html'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/115.0.0.0 Safari/537.36'}
r=requests.get(url,headers=headers)
from bs4 import BeautifulSoup
tf=BeautifulSoup(r.text,features="html.parser")
lis=tf.find_all('li',class_="")
headers2={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Cookie':'kg_mid=9911e6a369084543b93014feadb0e16a; kg_dfid=1bmkDh40J6tG3udvQV4IQYkV; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1688716656,1690792481'
}
for li in lis:
    if li.has_attr('data-eid'):
        temp_url='http://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id='+li.get('data-eid')
        temp_r=requests.get(temp_url,headers=headers2)
        print(temp_r.json()['data']['play_url'])
        print('-------------------------------')
