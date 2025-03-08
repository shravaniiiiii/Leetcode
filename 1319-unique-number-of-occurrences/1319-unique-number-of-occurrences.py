from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
      d={}
      for i in arr:
        if i in d:
          d[i]+=1
        else:
          d[i]=1
      s = list(d.values())
      return len(s)==len(set(s))