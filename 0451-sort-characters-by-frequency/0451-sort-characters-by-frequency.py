from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
      b=Counter(s)
      c=[]
      while b:
        maxi=max(b,key=b.get)
        c.append(maxi*b[maxi])
        del b[maxi]
      return ''.join(c)

        