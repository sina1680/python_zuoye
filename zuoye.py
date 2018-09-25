import sys
#更改作业完成状态
def change_state(zuoye,i):
    i=int(i)-1
    a=zuoye[i]
    zuoye.pop(i)
    a=a.replace('未完成','已完成')
    zuoye.insert(i,a)
    

math_zuoye=['《练习》第9，10页','订正周末作业练习卷和课堂作业本']

yuwen_zuoye=['背第5课6-8自然段','预习第6课','完成《默》第5课']

yingwen_zuoye=[]

ziran_zuoye=['完成课堂练习题，共4页','大部分有讲解，请检查，折去放教学书中']

changgui_zuoye=['读《同步》5课','背《古诗词》4首','跳绳10分钟']

zuoye=[]

zuoye_num=1
for i in math_zuoye:
    zuoye.append('作业号'+str(zuoye_num)+' 数学作业：'+i+' 未完成')
    zuoye_num=zuoye_num+1


yuwen_zuoye_num=1
for i in yuwen_zuoye:
    zuoye.append('作业号'+str(zuoye_num)+' 语文作业：'+i+' 未完成')
    zuoye_num=zuoye_num+1

yingwen_zuoye_num=1
for i in yingwen_zuoye:
    zuoye.append('作业号'+str(zuoye_num)+' 英语作业：'+i+' 未完成')
    zuoye_num=zuoye_num+1

ziran_zuoye_num=1
for i in ziran_zuoye:
    zuoye.append('作业号'+str(zuoye_num)+' 自然作业：'+i+' 未完成')
    zuoye_num=zuoye_num+1

changgui_zuoye_num=1
for i in changgui_zuoye:
    zuoye.append('作业号'+str(zuoye_num)+' 常规作业：'+i+' 未完成')
    zuoye_num=zuoye_num+1

isfinished=False
while not isfinished:
    a=0
    for i in zuoye:
        print(i+'\n')
        if i.find('未完成')>1:
            a=a+1
    if a>0:
        print('温馨提示：还有'+str(a)+'个作业未完成\n')
    else:
        print('恭喜你，所有的作业都完成了！！！')
        sys.exit()
    what_finished=input('请输入你已经完成的作业号：')
    if what_finished.isdigit() and int(what_finished)<=len(zuoye):
        change_state(zuoye,what_finished)
        
        print('好的，作业号'+str(what_finished)+'登记已完成\n')
    else:
        print('请输入正确的作业号\n')
    isfinished=False
