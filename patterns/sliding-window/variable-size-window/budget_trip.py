"""
PROBLEM STATEMENT:
A traveler is visiting attractions. Each attraction 'i' has a cost[i] and 
a time_spent[i]. Find the length and the actual subarray of the longest 
consecutive attractions where:
1. Total Cost is < 14 
AND 
2. Total Time Spent is < 20

INPUT:
- costs: List[int]
- times: List[int]

OUTPUT:
- (int, List[int]) -> (max_length, best_subarray_of_costs)

CONSTRAINTS:
- O(n) Time Complexity.
- All values are positive integers.

EXAMPLE:
Input: costs = [5, 5, 5, 2, 2], times = [10, 5, 2, 8, 8]
Output: (3, [5, 2, 2])
Explanation: [5, 5, 5] cost is 15 (> 14). [5, 2, 2] cost is 9 and time is 18.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils import *

class Solution():
    @measure
    def solve(self, params):
        # extract inputs needed for this problem
        costs = params["costs"]
        times = params["times"]
        


if __name__ == "__main__":
    params = parse_input_file("input.txt")

    result = Solution().solve(params)

    write_output(result)