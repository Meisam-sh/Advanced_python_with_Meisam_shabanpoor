from typing import OrderedDict
def scoreboard(Group_B,wins,loses,draws,goal_difference,points):
    sc_boad=OrderedDict()
    for k in range (len(Group_B)):
        sc_boad[Group_B[k]]=[wins[Group_B[k]],loses[Group_B[k]],draws[Group_B[k]],goal_difference[Group_B[k]],points[Group_B[k]]]
    sorted_sc_board = sorted(sc_boad.items(), key=lambda x: (-x[1][-1], -x[1][0], x[0]))  
    sorted_sc_board = OrderedDict(sorted_sc_board)  
    return (sorted_sc_board)
################################ definition of required dictionaries
result=OrderedDict()
wins=OrderedDict()
loses=OrderedDict()
draws=OrderedDict()
goal_difference=OrderedDict()
points=OrderedDict()
Group_B=['Iran','Spain','Portugal','Morocco']
####################################################### fill our dictionaries with zero
for i in range(len(Group_B)):
    wins[Group_B[i]]=0
    loses[Group_B[i]]=0
    draws[Group_B[i]]=0
    goal_difference[Group_B[i]]=0
    points[Group_B[i]]=0
######################################################### fill dictionaries based on input results
for i in range(len(Group_B)):
    for j in range(i+1,len(Group_B)):
        #print(f'{Group_B[i]}-{Group_B[j]}',i,' ',j)
        result[f'{i}-{j}']=list(map(int,input().split('-')))
        if result[f'{i}-{j}'][0]>result[f'{i}-{j}'][1]:
            wins[Group_B[i]]+=1
            loses[Group_B[j]]+=1
            goal_difference[Group_B[i]]+=result[f'{i}-{j}'][0]-result[f'{i}-{j}'][1]
            goal_difference[Group_B[j]]+=result[f'{i}-{j}'][1]-result[f'{i}-{j}'][0]
            points[Group_B[i]]+=3
        if result[f'{i}-{j}'][0]<result[f'{i}-{j}'][1]:
            wins[Group_B[j]]+=1
            loses[Group_B[i]]+=1
            goal_difference[Group_B[i]]+=result[f'{i}-{j}'][0]-result[f'{i}-{j}'][1]
            goal_difference[Group_B[j]]+=result[f'{i}-{j}'][1]-result[f'{i}-{j}'][0]
            points[Group_B[j]]+=3
        if result[f'{i}-{j}'][0]==result[f'{i}-{j}'][1]:
            draws[Group_B[i]]+=1
            draws[Group_B[j]]+=1
            points[Group_B[i]]+=1
            points[Group_B[j]]+=1
#################################
r=scoreboard(Group_B,wins,loses,draws,goal_difference,points)
for key,value in r.items():
    print(f'{key}  wins:{r[key][0]} , loses:{r[key][1]} , draws:{r[key][2]} , goal difference:{r[key][3]} , points:{r[key][4]}')