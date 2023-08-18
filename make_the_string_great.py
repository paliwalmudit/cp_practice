class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if stack and abs(ord(stack[-1])-ord(i))==32:
                stack.pop()
            else:stack.append(i)

        return ''.join(stack)