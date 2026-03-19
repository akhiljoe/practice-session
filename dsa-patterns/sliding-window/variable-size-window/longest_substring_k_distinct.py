#12
# Longest Substring With At Most K Distinct Characters

# Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.


# Example 1
# Input : s = "aababbcaacc" , k = 2
# Output : 6
# Explanation : The longest substring with at most two distinct characters is "aababb".
# The length of the string 6.

# Example 2
# Input : s = "abcddefg" , k = 3
# Output : 4
# Explanation : The longest substring with at most three distinct characters is "bcdd".
# The length of the string 4.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from utils import *

class Solution:
    @measure
    def solve(self, params):
        s = params["s"]
        k = params["k"]

        n = len(s)
        max_len = 0
        till_now = {}
        dist_char_count = 0
        left = 0
        for right in range(n):

            while dist_char_count >k:
                
                if till_now[s[left]]==1:
                    till_now.pop(s[left])
                    dist_char_count-=1
                else:
                    till_now[s[left]]-=1
                left+=1

            if till_now.get(s[right]) is not None:
                till_now[s[right]]+=1
            else:
                till_now[s[right]]=1
                dist_char_count+=1
            
            if dist_char_count<=k:
                max_len = max(max_len,right-left+1)
        
        return max_len
                


if __name__ == "__main__":
    params = parse_input_file()

    result = Solution().solve(params)

    write_output(result)