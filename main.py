#encoding = utf-8
import random
import math
import time
class SimulateAnealing():
    def __init__(self,T, a, Maximize_iteration,tbl):
        self.T = T
        self.a = a 
        self.Maximize_iteration = Maximize_iteration
        self.tbl = tbl;
        self.path = []
        for i in range(len(self.tbl[0])):
            self.path.append(i)
        self.path.append(self.path[0])
        self.value = 0
        for i in range(len(self.tbl[0])):
            self.value +=int(self.tbl[self.path[i]][self.path[i+1]])
        self.min_value = 0
        self.min_value =self.value 
        self.min_value_path = []
        self.min_value_path = self.path
    def solve(self):
        for i in range(0,self.Maximize_iteration):
            self.new_value = 0
            self.new_path = []
            self.x = 0
            self.y = 0
            self.tmp = 0
            self.delta = 0
            for j in range(len(self.path)):
                self.new_path.append(self.path[j])
            self.x = random.randint(1,len(self.path)-2)
            self.y = self.x 
            while self.y == self.x:
                self.y = random.randint(1,len(self.path)-2)
            self.tmp = self.new_path[self.x]
            self.new_path[self.x] = self.new_path[self.y]
            self.new_path[self.y] = self.tmp
            for j in range(len(self.tbl[0])):
                self.new_value += int(self.tbl[self.new_path[j]][self.new_path[j+1]])
            self.delta = self.new_value - self.value
            self.tmp = random.uniform(0,1)
            if self.delta < 0:
                print("iteration:",i,", because of ∆",self.delta,"<0, swithes.")
                self.path = self.new_path
                self.value = self.new_value
            elif self.tmp <= math.exp(-self.delta/self.T):
                print("iteration:",i,", because of p:",self.tmp,"<= exp(-∆/T)",math.exp(-self.delta/self.T)," switches.")
                self.path = self.new_path
                self.value = self.new_value 
            self.T *= self.a 
            if self.value < self.min_value:
                self.min_value = self.new_value 
                self.min_value_path = self.new_path
                print("New min value:",self.min_value,"founded, and its path:",self.min_value_path)
#read TSPtbl txt
s_time = time.time()
tbl = []
for f in open("gr17_d.txt","r",encoding ='UTF-8'):
    tbl.append(f.strip('\n').split(' '))
#initial SA algorithm
T = 100
a = 0.99 
n = 100000
prob = SimulateAnealing(T, a, n, tbl)
print(prob.path)
print("the initial value:", prob.value)
prob.solve()
print("approximate optimal solution value:",prob.min_value)
print("fitness function value:",prob.min_value_path)
print("running time", time.time()-s_time)
print("with T=",T,", cooling rate=",a,", n=",n,".")
