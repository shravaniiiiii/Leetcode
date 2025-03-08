class Solution:
    def secondHighest(self, s: str) -> int:
      b=set()
      s1=list(s)
      for i in s:
        if i.isdigit():
          b.add(int(i))
      b=sorted(b)
      if len(b)<=1:
        return -1
      return b[-2]
        