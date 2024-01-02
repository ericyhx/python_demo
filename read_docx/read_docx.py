# auth:eric.yu
# date: 2023/12/18 17:41

import re
from tkinter import *
import random

# 调用函数进行测试
#预赛
file_path="E:\舌战\shezhantiku.txt"
#决赛
#file_path="E:\舌战\juesai.txt"
text_list=[]
answer_list=[]
right_list=[]
global current_index
current_index = 148
p =re.compile(r'[（](.*?)[）]')
p2 = re.compile(r'[(](.*?)[)]')
# try:
with open(file_path,'r',encoding='utf-8') as file:
    for line in file:
        line=line.replace("\n",'')
        if len(line) <5:
            continue
        matches = re.findall(p, line)
        if len(matches)==0:
            matches = re.findall(p2, line)
        if len(matches)>0:
            temp_text=line
            for m in matches:
                new_text=temp_text.replace(m,"     ")
                temp_text=new_text
            question=new_text
        text_list.append(question)
        answer_list.append(line)
cnts=len(text_list)
def run1():
    lb4.configure(text='')
    lb2.configure(text='')
    index=random.randrange(0,cnts)
    if len(right_list) == cnts:
        lb1.configure(text="已全部测试完成")
        inp1.delete(0,END)
        return
    while right_list.__contains__(index):
        index = random.randrange(0, cnts)
    global current_index
    current_index=index
    lb1.configure(text=text_list[index])
    inp1.delete(0, END)
    lb0.configure(text=f"共{len(text_list)}题，还剩{len(text_list)-len(right_list)}题")



def run2():
    global current_index
    lb4.configure(text=f"答案：{answer_list[current_index]}", fg='blue')

def run3():
    ans=inp1.get()
    anss=ans.split("，")
    global current_index
    question = text_list[current_index]
    matches = re.findall(p, question)
    if len(matches) == 0:
        matches = re.findall(p2, question)
    if len(matches) > 0:
        temp_text = question
        temp_index=0
        for m in matches:
            new_text = temp_text.replace(m, anss[temp_index],1)
            temp_text = new_text
            temp_index=temp_index+1
        if temp_text.__eq__(answer_list[current_index]):
            lb2.configure(text='正确', fg='green')
            if not right_list.__contains__(current_index):
                right_list.append(current_index)
        else:
            lb2.configure(text='错误', fg='red')

root=Tk()
root.geometry('800x240')
root.title('题目测试')

lb0=Label(root,text=f"共{len(text_list)}题，还剩{len(text_list)-len(right_list)}题")
lb0.place(relx=0,rely=0,relwidth=0.2,relheight=0.1)
lb1=Label(root,text=text_list[current_index],wraplength=700)
lb1.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.2)
inp1=Entry(root)
inp1.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.1)

lb2=Label(root)
lb2.place(relx=0.6,rely=0.3,relwidth=0.2,relheight=0.1)

btn1=Button(root,text="提交",command=run3)
btn1.place(relx=0.2,rely=0.5,relwidth=0.1,relheight=0.1)

btn2=Button(root,text="答案",command=run2)
btn2.place(relx=0.4,rely=0.5,relwidth=0.1,relheight=0.1)

btn2=Button(root,text="下一题",command=run1)
btn2.place(relx=0.6,rely=0.5,relwidth=0.1,relheight=0.1)

lb3=Label(root,text="===================================================================================================================")
lb3.place(relx=0,rely=0.6,relwidth=1,relheight=0.1)


lb4=Label(root,wraplength=700)
lb4.place(relx=0.05,rely=0.7,relwidth=0.9,relheight=0.3)


root.mainloop()
