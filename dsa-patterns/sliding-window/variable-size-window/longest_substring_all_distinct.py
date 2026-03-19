# Longest Substring With No Repeating Characters

# Given a string s, find the length of the longest substring with no repeating characters


# Example 1
# Input : s = "aababbcaacc"
# Output : 3

# Example 2
# Input : s = "abcddefg"
# Output : 4

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from utils import *

class Solution:
    @measure
    def solve(self, params):
        s = params["s"]

        n = len(s)
        max_len = 0
        till_now = {}
        left = 0
        for right in range(n):
            while s[right] in till_now:
                till_now.pop(s[left])
                left+=1
            max_len = max(max_len,right-left+1)
            till_now[s[right]] = True

        return max_len


if __name__ == "__main__":
    params = parse_input_file()

    result = Solution().solve(params)

    write_output(result)