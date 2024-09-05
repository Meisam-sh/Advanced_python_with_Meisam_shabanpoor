from statistics import mean
class school:
    def __init__(self,name,age,hight,weight,n):
        self.name=name
        self.age=age
        self.hight=hight
        self.weight=weight
        self.n=n        
    def calculate_avg(self):
        mean_age=self.age/self.n
        mean_hight=self.hight/self.n
        mean_weight=self.weight/self.n
        print(mean_age)
        print(mean_hight)
        print(mean_weight)
        return(mean_age,mean_hight,mean_weight)
    def top_class(meana,meanb):
        if meana[0]>meanb[0]:
            print("A")
        elif meana[0]<meanb[0]:
            print("B")
        elif meana[0]==meanb[0] and meana[1]>meanb[1]:
            print("A")
        elif meana[0]==meanb[0] and meana[1]<meanb[1]:
            print("B")
        else:
            print("Same")
            



xA=int(input())
age=input().split(' ')
hight=input().split(' ')
weight=input().split(' ')
A_age=[]
A_hight=[]
A_weight=[]
for i in range(xA):
    A_age.append(int(age[i]))
    A_hight.append(int(hight[i]))
    A_weight.append(int(weight[i]))

###################################33
xB=int(input())
age=input().split(' ')
hight=input().split(' ')
weight=input().split(' ')
B_age=[]
B_hight=[]
B_weight=[]
for i in range(xA):
    B_age.append(int(age[i]))
    B_hight.append(int(hight[i]))
    B_weight.append(int(weight[i]))
a=school('A',sum(A_age),sum(A_hight),sum(A_weight),xA)
b=school('B',sum(B_age),sum(B_hight),sum(B_weight),xB)
a_avg=a.calculate_avg()
b_avg=b.calculate_avg()
m=school.top_class(a_avg[1:],b_avg[1:])