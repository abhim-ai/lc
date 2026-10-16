class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left=0
        best_len=0
        char_count={}
        for right in range(len(s)):
            r_char=s[right]
            char_count[r_char]=char_count.get(r_char,0)+1

            while len(char_count)>k:
                l_char=s[left]
                char_count[l_char]-=1
                if char_count[l_char]==0:
                    del char_count[l_char]
                left+=1
            best_len=max(best_len,right-left+1)

        return best_len        