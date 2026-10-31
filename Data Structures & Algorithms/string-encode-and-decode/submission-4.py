class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s = s + strs[i] + "-"
        return s

    def decode(self, s: str) -> List[str]:
        fr = []
        temp = ""
        for char in s:
            if char != "-":
                temp += char
            else:
                fr.append(temp)
                temp = ""
        
        return fr