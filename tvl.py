import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus']=False
'''一、長攻、對角和攔中三個位置的得分方式有哪些不同？'''
player=[]
with open('tvl-ctvba-2017-2019-2.txt',encoding='utf8') as f:
    for line in f:
        player.append(line.split())

playerSet = ['長攻','對角','攔中']
Attack=[]
Block=[]
Serve=[]
for e in playerSet:
    attack=block=serve=0
    Num=0
    for i in player:
        if i[6]==e:
            attack+=float(i[-5])/float(i[-2])
            block+=float(i[-4])/float(i[-2])
            serve+=float(i[-3])/float(i[-2])
            Num+=1
    Attack.append(attack/Num)    
    Block.append(block/Num)    
    Serve.append(serve/Num)    
    
    print(e+'得分方式中, 攻擊:攔網:發球=',round(attack/Num,2),' : ',round(block/Num,2),' : ',round(serve/Num,2))
    
'''攻擊得分長條圖'''
plt.bar(range(len(playerSet)),Attack,width=0.3)
fig=plt.gcf()
plt.xticks(range(len(playerSet)),playerSet)
plt.title('長攻、對角、攔中的攻擊得分比例',loc='left')
plt.ylim(0.5,1)
fig.set_size_inches(10, 10)

plt.savefig('Attack.png')
plt.clf()

'''攔網得分長條圖'''
plt.bar(range(len(playerSet)),Block,width=0.3)

plt.xticks(range(len(playerSet)),playerSet)
plt.title('長攻、對角、攔中的攔網得分比例',loc='left')
fig.set_size_inches(10, 10)

plt.savefig('Block.png')
plt.clf()

'''發球得分長條圖'''
plt.bar(range(len(playerSet)),Serve,width=0.3)

plt.xticks(range(len(playerSet)),playerSet)
plt.title('長攻、對角、攔中的發球得分比例',loc='left')
fig.set_size_inches(10, 10)

plt.savefig('Serve.png')
plt.clf()
    
'''二、參賽隊伍攻擊、防守能力與排名的關係'''
team=[]
teamNum=[]
allAttack=allBlock=0
teamAttack=[]
teamBlock=[]
for p in player[1:]:
    if p[2] in team:
        
        teamNum[team.index(p[2])]+=1
    else:
        team.append(p[2])
        teamNum.append(1)

for t in team:

    attack=block=0
    for p in player:
        if p[2] == t:
                attack+=float(p[-5])/float(p[-2])
                block+=float(p[-4])/float(p[-2])
    teamAttack.append(attack/teamNum[team.index(t)])
    teamBlock.append(block/teamNum[team.index(t)])
    print(t,round(attack/teamNum[team.index(t)],2),' : ',round(block/teamNum[team.index(t)],2))
    allAttack+=round(attack/teamNum[team.index(t)],2)
    allBlock+=round(block/teamNum[team.index(t)],2)
    
print('平均攻擊得分比例 : ',round(allAttack/len(team),2))  
print('平均攔網得分比例 : ',round(allBlock/len(team),2))  

'''攻擊得分比例長條圖'''
plt.figure(figsize=(10,10))

plt.bar(range(len(team)),teamAttack)

plt.axhline(y=0.83,c='r',ls='--')
plt.xticks(range(len(team)),team)
plt.yticks([0.5,0.6,0.7,0.8,0.83,0.9,1])
plt.ylim(0.5,1)
plt.title('各隊總得分中攻擊得分所占比例',loc='left')
plt.tick_params(axis='x', labelrotation=-60)
fig.set_size_inches(10, 10)
plt.savefig('teamAttack.png')
plt.clf()

'''攔網得分比例長條圖'''
plt.bar(range(len(team)),teamBlock)

plt.axhline(y=0.12,c='r',ls='--')
plt.yticks([0.025,0.050,0.075,0.100,0.120,0.125,0.150,0.175,0.200])
plt.xticks(range(len(team)),team)
plt.title('各隊總得分中攔網得分所占比例',loc='left')
plt.tick_params(axis='x', labelrotation=-60)
fig.set_size_inches(10, 10)
plt.savefig('teamBlock.png')

    
