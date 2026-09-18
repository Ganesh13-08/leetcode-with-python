class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        add = 0
        add2 = 0
        for i in s:
            add += ord(i)
        for i in t:
            add2 += ord(i)
        return chr(add2-add)