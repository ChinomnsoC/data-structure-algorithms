class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have_map = {}
        t_map = {}

        left, right, formed = 0, 0, 0
        min_length = float("inf")
        min_start = 0

        # create t_map

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        required = len(t_map)

        for right in range(len(s)):
            curr_char = s[right]
            if curr_char in t_map:
                have_map[curr_char] = have_map.get(curr_char, 0) + 1
                char_have = have_map[curr_char]

                if char_have == t_map[curr_char]:
                    formed += 1

            while formed == required:
                window_size = right - left + 1

                if window_size < min_length:
                    min_length = window_size
                    min_start = left

                left_char = s[left]
                if left_char in have_map:
                    have_map[left_char] -= 1
                    if left_char in t_map and have_map[left_char] < t_map[left_char]:
                        formed -= 1
                left += 1

        return s[min_start : min_start + min_length] if min_length != float('inf') else ""
