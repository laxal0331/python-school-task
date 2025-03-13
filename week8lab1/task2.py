class Animal:
    def __init__(self,arms,legs):
        self.arms = arms
        self.legs = legs
    def lims(self):
        return self.arms+self.legs
spider=Animal(4,4)
spiderlimbs=spider.lims()
print(spiderlimbs)