class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        words = s.split()
        last_word = words[-1]
        return len(last_word)