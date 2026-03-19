# Problem Statement
# Given an integer array nums and an integer target, return all unique pairs of integers $[a, b]$ such that $a + b = target$. 
# Each pair in the output must be unique, meaning $[1, 2]$ and $[2, 1]$ are considered the same pair and should only be returned once.

# Input: nums = [1, 1, 2, 4, 3, 3], 
# target = 4
# Output: [[1, 3]]

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils import *

class Solution():
    def solve(self, params):
        # extract inputs needed for this problem
        nums = params["nums"]
        target = params["target"]

        result = []
        


if __name__ == "__main__":
    params = parse_input_file("input.txt")

    result = Solution().solve(params)

    write_output(result)