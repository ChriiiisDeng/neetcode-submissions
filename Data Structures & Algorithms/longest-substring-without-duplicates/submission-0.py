class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        left = 0
        length = len(s)
        max_length = 0
        for right in range(length):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            max_length = max(max_length, right - left + 1)
            char_set.add(s[right])

        return max_length
        