class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        chat_count = defaultdict(int)
        for ch in t:
            chat_count[ch] += 1


        char_remaining = len(t)
        min_window = (0, float("inf"))
        left = 0

        for right, ch in enumerate(s):
            if chat_count[ch] > 0:
                char_remaining -= 1
            
            chat_count[s[right]] -= 1


            if char_remaining == 0:
                # match conditon ,shrink the window to get minimun

                while True:
                    char_start = s[left]
                    if chat_count[char_start] == 0:
                        # need this charecter
                        break

                    chat_count[char_start] += 1
                    left += 1

                if right - left < min_window[1] - min_window[0]:
                    min_window = (left, right)

                chat_count[s[left]] += 1
                char_remaining += 1
                left += 1



        return "" if min_window[1] > len(s) else s[min_window[0] : min_window[1] + 1]

        