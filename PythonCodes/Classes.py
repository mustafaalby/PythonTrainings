#%%
#constructor class
class Worker:
    salary_update=1.6
    counter=0
    def __init__(self,name,surname,salary):
        self.name=name
        self.surname=surname
        self.salary=salary
        Worker.counter=Worker.counter+1
    
    def printName(self):
        return self.name+" "+self.surname
    def update(self):
        self.salary=self.salary+self.salary



#%%
