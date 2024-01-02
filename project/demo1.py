
'''第一种'''
fp=open('D:/test.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()
'''第二种'''
with open('D:/test.txt','w') as file:
    file.write("奋斗成就更改的你！")

if __name__ == '__main__':
    url ='https://hey10.cjkypo.com/20230323/eDgHWWob/1000kb/hls/06RHPsm6.ts'
    print(url.split("/")[-1:])


