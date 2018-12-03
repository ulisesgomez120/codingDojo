class Math_dojo:
    def __init__(self):
        self.global_sum = 0
    def __basic_add(self,*nums): 
        sum = 0 
        for num in nums[0]:
            sum += num
        return sum
    def add(self,*nums):
        x = self.__basic_add(nums)
        self.global_sum += x
        return self
    def subtract(self,*nums):
        y = self.__basic_add(nums)
        self.global_sum -= y
        return self
    def result(self):
        return self.global_sum
md = Math_dojo()
x = md.add(2).add(2,5,1).subtract(3,2).result()
print(x)
