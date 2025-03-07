class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      tsum=sum(nums)
      lsum=0
      for i in range(len(nums)):
        if lsum==(tsum-lsum-nums[i]):
          return i
        lsum+=nums[i]
      return -1

          
  
        


        