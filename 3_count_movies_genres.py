from typing import OrderedDict
gener=['Horror', 'Romance', 'Comedy', 'History' , 'Adventure' , 'Action']
genercounter=OrderedDict()
for j in range(0,len(gener)):
    genercounter[gener[j]]=0
n=int(input())
favorite=[]
for i in range (n):
    favorite=input().split()
    for j in range(0,len(gener)):
        if gener[j]  in favorite:
            genercounter[gener[j]]+=1
sorted_genercounter = OrderedDict(sorted(genercounter.items(), key=lambda x: (-x[1], x[0])))
for genre, count in sorted_genercounter.items():
    print(f"{genre} : {count}")
