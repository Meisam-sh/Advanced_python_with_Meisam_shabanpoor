class person:
    def __init__(self,name,family):
        self.name=name
        self.family=family
    def father(self):
        print("%s %s is the father of this family" % (self.name,self.family))
x=input().split()
p=person(x[0],x[1])
p.father()