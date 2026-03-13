# Find the length of the longest subarray where sum < 14

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
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
    params = parse_input_file("input.txt")

    result = Solution().solve(params)

    write_output(result)
