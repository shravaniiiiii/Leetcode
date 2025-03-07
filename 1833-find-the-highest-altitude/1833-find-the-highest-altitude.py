class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
      b=[0]
      for i in range(len(gain)):
        c=gain[i]
        b.append(b[i]+c)
      return max(b)


        