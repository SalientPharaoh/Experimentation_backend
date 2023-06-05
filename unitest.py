import random
from datetime import datetime

class profiles():
    def __init__(self):
        self.options=["AA","AAwL","AT","ATwL","TA","TAwL","TT","TTwL"]
        self.choice=""
    def select(self):
        self.choice= random.choice(self.options)
        return self.choice
    

d={"AA":0,"AAwL":0,"AT":0,"ATwL":0,"TA":0,"TAwL":0,"TT":0,"TTwL":0}

for i in range(100):
    obj=profiles()
    d[obj.select()]+=1

print(d)

print(datetime.now().strftime("%d/%m/%Y"))