# auth:eric.yu
# date: 2023/7/28 16:52

"""
getcwd()                            返回当前的工作目录
listdir(path)                       返回指定路径下的二五年间和目录信息
mkdir(path[,mode])                  创建目录
makedirs(path1/path2...[,mode])     创建多级目录
rmdir(path)                         删除目录
removedirs(path1/path2....)         删除多级目录
chdir(path)                         将path设置为当前工作目录
"""
import os

print(os.getcwd())
lst=os.listdir("../chap6")
print(lst)
os.mkdir("newdir")
os.rmdir("newdir")
