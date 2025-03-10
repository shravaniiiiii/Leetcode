class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      n=len(nums)
      nums.sort()
      dp=[set()]
      dp[0].add(())
      for i in nums:
        n_s=set()
        for s in dp[-1]:
          n_s.add(s+(i,))
        dp.append(dp[-1]|n_s)
      return [list(s) for s in dp[-1]]