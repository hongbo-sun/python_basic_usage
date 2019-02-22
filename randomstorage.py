import random

class RandomStorage:

    chucun=[]
    def set (self,shuru):
        if self.find(shuru):
            pass
        else:
            self.chucun.append(shuru)
        
    def get (self):
        size=len(self.chucun)
        a=random.randint(0,size-1)
        zhi=self.chucun[a]
        del self.chucun[a]
        return zhi
    
    def find(self,shuru):
        if shuru in self.chucun:
            return True
        else:
            return False
        

    def __init__(self):
        pass
       
        
        

        
if __name__ == '__main__':
    k=RandomStorage()
    '''
    k.set(5)
    k.set(2)
    '''
    #zhi=k.get()

    #print(zhi)
    
    print(k.chucun)
    print(k.find(5))
    k.set(2)
    print(k.chucun)

