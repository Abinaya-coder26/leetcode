class Solution:
    def isMatch(self, s, p):
        if not p:
            return not s

        first = bool(s) and (s[0] == p[0] or p[0] == '.')

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or 
                    (first and self.isMatch(s[1:], p)))
        else:
            return first and self.isMatch(s[1:], p[1:])