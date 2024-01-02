# auth:eric.yu
# date: 2023/9/1 15:43
import datetime
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from tqdm import tqdm




headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
pre_url="https://hey11.cjkypo.com/202308/26/RGkvPL2W8P3/video/1000k_0X720_64k_25/hls/player"
pre_ts_path="E:\\move_ts\\"
ts_path="E:\\move_ts\\"
out_file_path="E:\\move_ts\\坚如磐石.mp4"
ts_list_file_path="E:\\move_ts\\file_list.txt"
success_ts=[]
def download(player:dict):
    name = player.get("name")
    url = player.get("url")
    ret=request_ts(0,url,name)
    if ret == -1:
        return
def request_ts(cnt,url,name):
    try:
        r = requests.get(url, headers=headers)
        with open(pre_ts_path + name, 'wb') as f:
            f.write(r.content)
            success_ts.append(name)
        return 0
    except Exception:
        cnt=cnt+1
        time.sleep(3)
        if cnt >10:
            print(f"{name}文件下载出错，重试失败")
            with open('download_fail.txt','wb') as f:
                f.write(name+"\n")
            return -1
        print(f"{name}文件下载出错，对进行第{cnt}次重试")
        return request_ts(cnt,url,name)
def generator_movie():
    file_names = os.listdir(ts_path)
    if os.path.exists(ts_list_file_path):
        os.remove(ts_list_file_path)
    with open(ts_list_file_path,"w+") as f:
        for name in file_names:
            sufix = os.path.splitext(name)[-1:]
            if(".ts" not in sufix):
               continue
            f.write("file '" + name + "'\n")
    print("生成txt文件成功!")
    start = datetime.datetime.now()
    print('开始合成，初始时间为:', start)
    cmd='ffmpeg -f concat -safe 0 -i ' + ts_list_file_path + ' -c ' + ' copy ' + out_file_path
    print(f"cmd:{cmd}")
    os.system(cmd)
    print('合成后的当前时间为：', datetime.datetime.now())
    print('合成视频完成！用时：' + str(datetime.datetime.now() - start))
def test(i):
    c=0
    name= threading.current_thread().getName()
    while c<20:
        print(f"{name}|i={i}当前值：{c}")
        time.sleep(1)
        c=c+1
def main(lst):
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download,lst)
def remove_ts():
    file_names = os.listdir(ts_path)
    for name in file_names:
        sufix = os.path.splitext(name)[-1:]
        if ".ts" in sufix:
            os.remove(ts_path + name)
def getTsList(url):
    r = requests.get(url, headers=headers)
    lst = []
    i=1;
    for s in r.text.split("\n"):
        if s.endswith(".ts"):
            s="https://vip3.49zyvideoplayurl.com"+s
        # if s.startswith("https"):
            if i <10:
                idx='000'+str(i)
            elif i <100:
                idx = '00' + str(i)
            elif i < 1000:
                idx = '0' + str(i)
            else:
                idx = str(i)
            player={"url":s,"name":"player"+idx+".ts"}
            lst.append(player)
            i=i+1
    return lst
def monitor_process(count):
    pbar = tqdm(total=count)
    while len(success_ts) < count:
        time.sleep(0.2)
        pbar.update(1)
        pbar.set_description("Processing %d" % len(success_ts))  # 执行循环体内的代码
    pbar.close()

if __name__ == '__main__':
    remove_ts()
    m3u8_url="https://vip3.49zyvideoplayurl.com/20231214/XPqvR3Zx/2000kb/hls/index.m3u8"
    lst=getTsList(m3u8_url)
    start = datetime.datetime.now()
    print('开始下载，初始时间为:', start)
    monitor = threading.Thread(target=monitor_process, args=(len(lst),))
    monitor.start()
    main(lst)
    print('下载完成！用时：' + str(datetime.datetime.now() - start))
    generator_movie()
    remove_ts()
