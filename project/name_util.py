# auth:eric.yu
# date: 2023/8/31 16:52
import datetime
import os

file_path="E:\\move_ts\\"
out_file_name='巨齿鲨_深渊.mp4'
print(len(os.listdir(file_path)))
file_names=os.listdir(file_path)
f=open(file_path+"file_list.txt",'w+')
for name in file_names:
    f.write("file '" + name + "'\n")
f.close()
print("生成txt文件成功!")
start = datetime.datetime.now()
print('开始合成，初始时间为:',start)
ffmpeg_bin_dic = 'D:\\Program Files\\ffmpeg-win64\\bin\\'
os.system('ffmpeg -f concat -safe 0 -i '+file_path+'file_list.txt'+' -c '+ ' copy ' +file_path+ out_file_name)
print('合成后的当前时间为：', datetime.datetime.now())
print('合成视频完成！用时：' + str(datetime.datetime.now() - start))
cmd="ffmpeg -f concat -safe 0 -i E:\\move_ts\\file_list.txt -c copy E:\\move_ts\\速度与激情10.mp4"
