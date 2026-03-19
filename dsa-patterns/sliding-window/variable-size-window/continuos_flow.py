# Find the length of the longest subarray where sum < 14

# Example 1
# Input : nums = [2, 1, 3, 4, 2, 1] , target = 14
# Output : 5
# Explanation : The longest subarray with sum < 14 is [2, 1, 3, 4, 2].
# Its sum is 12 and length is 5.

# Example 2
# Input : nums = [5, 1, 2, 3, 1, 1, 1] , target = 7
# Output : 4
# Explanation : The longest subarray with sum < 7 is [2, 3, 1, 1].
# Its sum is 7 (allowed since condition is > target to shrink), length is 4.

# Example 3
# Input : nums = [10, 2, 3] , target = 5
# Output : 2
# Explanation : The longest subarray with sum < 5 is [2, 3].
# Its sum is 5 and length is 2.

# Example 4
# Input : nums = [1, 1, 1, 1, 1] , target = 3
# Output : 3
# Explanation : The longest subarray with sum < 3 is [1, 1, 1].
# Its sum is 3 and length is 3.

# Example 5
# Input : nums = [4, 2, 2, 1, 1] , target = 6
# Output : 3
# Explanation : The longest subarray with sum < 6 is [2, 2, 1].
# Its sum is 5 and length is 3.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from utils import *
from collections import deque

class Solution():
    @measure
    def solve(self, params):
        # extract inputs needed for this problem
        nums = params["nums"]
        target = params["target"]
        n=len(nums)
        best_subarray = []
        current_sum = 0
        left = 0
        maxlength = 0
        for right in range(n):
            current_sum += nums[right]

            while current_sum>target:
                current_sum-=nums[left]
                left+=1

            current_len = right-left+1
            if current_len>maxlength:
                maxlength = current_len
                best_subarray = nums[left:right+1]
            
        return maxlength, best_subarray



if __name__ == "__main__":
    params = parse_input_file()

    result = Solution().solve(params)

    write_output(result)
