class Solution:
    def minWindow(self, s, t):
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        required = len(t)
        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in need:
                if need[ch] > 0:
                    required -= 1
                need[ch] -= 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_ch = s[left]

                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] > 0:
                        required += 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]