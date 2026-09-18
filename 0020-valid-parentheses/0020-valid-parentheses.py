class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif i==']':
                if not stack or stack[-1]!='[':
                    return False
                stack.pop()
            elif i=='}':
                if not stack or stack[-1]!='{':
                    return False
                stack.pop()
            elif i==')':
                if not stack or stack[-1]!='(':
                    return False
                stack.pop()
        if len(stack)==0:
            return True
        else:
            return False
