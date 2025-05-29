class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      a=[]
      for i in nums:
        index=abs(i) - 1
        if nums[index]<0:
          a.append(abs(i))
        else:
          nums[index]=-1*nums[index]
      return a

        

        