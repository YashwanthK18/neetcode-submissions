class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in strs:
            ans+=i
            ans+="xyzabd"
        return ans

    def decode(self, s: str) -> List[str]:
        return s.split("xyzabd")[:-1]
