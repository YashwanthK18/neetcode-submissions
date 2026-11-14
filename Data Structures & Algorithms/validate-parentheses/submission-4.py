class Solution:
    def isValid(self, se: str) -> bool:
        s=[]
        for i in se:
            if s and ((i=="]" and s[-1]=="[") or (i=="}" and s[-1]=="{") or (i==")" and s[-1]=="(")):
                s.pop()
            else:
                s.append(i)
        return not s