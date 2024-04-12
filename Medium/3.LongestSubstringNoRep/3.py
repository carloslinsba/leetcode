class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_max=""
        current_s=""
        for i in range(0,len(s)):
            if s[i] in current_s:
                if len(s_max)<len(current_s):
                    s_max=current_s
                while s[i] in current_s:
                    current_s = current_s[1:]
            current_s=current_s+s[i]
        if len(current_s)> len(s_max):
            return len(current_s)
        return len(s_max)


s = "ohvhjdml"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))