class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
    
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                r = s.pop()
                l = s.pop()
                if i == "+":
                    s.append(l+r)
                elif i == "-":
                    s.append(l-r)
                elif i == "*":
                    s.append(l*r)
                elif i == "/":
                    s.append(int(l/r))
            else:
                s.append(int(i))
        return s[0]