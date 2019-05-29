# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(pattern)==0 and len(s)==0:
            return True
        if len(pattern)==0 and len(s)>0:
            return False
        if len(pattern)>1 and pattern[1]=="*":
            if len(s)>0 and ( s[0]==pattern[0] or pattern[0]=='.'):
                return self.match(s[1:],pattern) or self.match(s,pattern[2:])
            else:
                return self.match(s,pattern[2:])
        if len(s)>0 and ( s[0]==pattern[0] or pattern[0]=='.'):
            return self.match(s[1:],pattern[1:])
        else:
            return False
