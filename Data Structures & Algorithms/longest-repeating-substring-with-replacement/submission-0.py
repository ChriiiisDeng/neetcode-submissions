class Solution:
   def characterReplacement(self, s: str, k: int) -> int:

        left, res = 0,0
        bucket = [0] * 26
        max_freq = 0
        for right in range(len(s)):
            bucket[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, bucket[ord(s[right]) - ord('A')])

            while (right - left + 1) - max_freq > k :
                # shrink window
                bucket[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
        