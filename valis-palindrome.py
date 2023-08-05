class Solution(object):
    def isPalindrome(self, s):
        punctuations = '''!()-[]{};:'`"\,<>./?@#$%^&*_~'''
        result = "".join([c.lower() for c in s if c not in punctuations])
        result = result.replace(" ", "")
        if(result==result[-1::-1]):return True
        else:return False