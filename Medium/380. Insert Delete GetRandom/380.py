import random

class RandomizedSet:
    s = dict()
    def __init__(self):
        self.s = dict()

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s[val]=1
        return True
        

    def remove(self, val: int) -> bool:
        if self.s.get(val):
            self.s.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        l= len(self.s)
        i = int(random.uniform(0,l))
        return list(self.s)[i]
        
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
param_2 = obj.remove(1)
param_1 = obj.insert(2)
print (obj.getRandom())