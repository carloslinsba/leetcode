class KthLargest:
    kth=[]
    k=None
    
    def __init__(self, k: int, nums: list[int]):
        self.k=k
        self.kth = []
        for idx,item in enumerate(nums):
            if idx<k:
                self.kth.append(item)
                if idx==k-1:
                    self.kth.sort(reverse=True)
            elif item>self.kth[k-1]:
                self.kth.pop()
                self.kth.append(item)
                self.kth.sort(reverse=True)        
        return None

    def add(self, val: int) -> int:
        if len(self.kth)<self.k:
            self.kth.append(val)
            self.kth.sort(reverse=True)
            return self.kth[len(self.kth)-1]
        elif val > self.kth[self.k-1]:
            self.kth.pop()
            self.kth.append(val)
            self.kth.sort(reverse=True)        
        return self.kth[self.k-1]

        


