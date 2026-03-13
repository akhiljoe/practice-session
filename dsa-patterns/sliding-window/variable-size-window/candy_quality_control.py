"""
VARIATION 1: QUALITY CONTROL (The "Counting" Twist)
Core Concept: Sliding Window with Frequency Counting.

PROBLEM STATEMENT:
You are a QA engineer at a candy factory. Given an array of strings 'candies', 
find the length of the longest continuous sequence you can pick such that 
the count of "Sour" candies in that sequence is STRICTLY LESS than 3.

INPUT: 
- candies: List[str]
- target_limit: int (e.g., 3)

OUTPUT: 
- int (The maximum length)

CONSTRAINTS:
- n <= 10^5
- Extra space: O(1) (excluding input)

EXAMPLE:
Input: candies = ["Sweet", "Sour", "Sweet", "Sour", "Sweet", "Sweet", "Sour", "Sweet"], target = 3
Output: 6
Explanation: ["Sweet", "Sour", "Sweet", "Sour", "Sweet", "Sweet"] contains 2 "Sour" candies.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils import *

class Solution():
    @measure
    def solve(self, params):
        # extract inputs needed for this problem
        candies = params["candies"]
        target = params["target"]

        n = len(candies)
        left = 0
        sour_count = 0
        maxlen = 0
        for right in range(n):
            if candies[right]=="Sour":
                sour_count+=1
            
            while sour_count>=target:
                if candies[left]=="Sour":
                    sour_count-=1
                left+=1

            maxlen = max(maxlen,right-left+1)
        return maxlen

if __name__ == "__main__":
    params = parse_input_file("input.txt")

    result = Solution().solve(params)

    write_output(result)