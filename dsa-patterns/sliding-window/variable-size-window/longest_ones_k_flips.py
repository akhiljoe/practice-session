# Given a binary array nums and an integer k, flip at most k 0's.

# Return the maximum number of consecutive 1's after performing the flipping operation.


# Example 1
# Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3
# Output : 10
# Explanation : The maximum number of consecutive 1's are obtained only if we flip the 0's present at position 3, 4, 5 (0 base indexing).
# The array after flipping becomes [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0].
# The number of consecutive 1's is 10.

# Example 2
# Input : nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3
# Output : 9
# Explanation : The underlines 1's are obtained by flipping 0's in the new array.
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1].
# The number of consecutive 1's is 9.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from utils import *

class Solution():
    @measure
    def solve(self, params):
        # extract inputs needed for this problem
        nums = params["nums"]
        k = params["k"]

        n = len(nums)
        max_len = 0
        zero_count = 0
        left = 0
        for right in range(n):
            if nums[right]==0:
                zero_count+=1

            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
                
            max_len = max(max_len,right-left+1)
        return max_len

if __name__ == "__main__":
    params = parse_input_file("input.txt")

    result = Solution().solve(params)

    write_output(result)