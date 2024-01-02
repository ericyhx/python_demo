# auth:eric.yu
# date: 2023/8/18 10:48
import numpy as np
max =0;
result=[]
with open('D:\\SI RMS Integration & Project\\winco\\818\\3411305_location.txt','r',encoding='utf-8') as f:
    lines=f.readlines();
    for l in lines:
        temp=l.split('location:[')
        t_max=len(temp[0])
        if temp[0].__contains__("send RobotFunctionPacket RobotFunctionPacket"):
            t_max=t_max+2
        if t_max < 320:
            s=""
            for i in range(320-t_max):
                s=s+" ";
            result.append(l.replace('location:[',s+"location:["))
    with open('D:\\SI RMS Integration & Project\\winco\\818\\3411305_location_format.txt','w',encoding='utf-8') as f2:
        for r in result:
            f2.write(r)
