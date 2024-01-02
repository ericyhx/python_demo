# auth:eric.yu
# date: 2023/9/1 15:43
import datetime
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from tqdm import tqdm



headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/115.0.0.0 Safari/537.36'}
pre_url="https://vip.lz-cdn1.com/20220322/357_54d1222c/1200k/hls/eef1dc7de7d00"
pre_ts_path="E:\\move_ts\\player"
ts_path="E:\\move_ts\\"
out_file_path="E:\\move_ts\\黑蟹行动.mp4"
ts_list_file_path="E:\\move_ts\\file_list.txt"
success_ts=[]
# def download(start:int,end:int):
#     for i in range(start, end):
#         name = ""
#         if i < 10:
#             name = "000" + str(i)
#         elif i < 100:
#             name = "00" + str(i)
#         elif i < 1000:
#             name = "0" + str(i)
#         else:
#             name = str(i)
#         url = pre_url + name + '.ts'
#         ret=request_ts(0,url,name)
#         if ret == -1:
#             return
def download(name_num:int):
    if name_num < 10:
        name = "000" + str(name_num)
    elif name_num < 100:
        name = "00" + str(name_num)
    elif name_num < 1000:
        name = "0" + str(name_num)
    else:
        name = str(name_num)
    url = pre_url + name + '.ts'
    # url = pre_url + str(name_num) + '.ts'
    ret=request_ts(0,url,name)
    if ret == -1:
        return
def request_ts(cnt,url,name):
    try:
        r = requests.get(url, headers=headers)
        with open(pre_ts_path + name + '.ts', 'wb') as f:
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

def monitor_process(count):
    pbar = tqdm(total=count)
    while len(success_ts) < count:
        time.sleep(0.2)
        pbar.update(1)
        pbar.set_description("Processing %d" % len(success_ts))  # 执行循环体内的代码
    pbar.close()


if __name__ == '__main__':
    remove_ts()
    count = 1705
    lst=list(range(1,count))
    start = datetime.datetime.now()
    print('开始下载，初始时间为:', start)
    monitor=threading.Thread(target=monitor_process,args=(count-1,))
    monitor.start()
    main(lst)
    print('下载完成！用时：' + str(datetime.datetime.now() - start))
    generator_movie()
    remove_ts()
