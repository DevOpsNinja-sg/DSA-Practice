class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s)!=len(t):
        return False
       tracker = {}
       for i in s:
        if i in tracker:
            tracker[i]+=1
        else:
            tracker[i]=1
       
       for c in t:
        if c not in tracker or tracker[c]==0:
            return False
        tracker[c]-=1
       return True
        
