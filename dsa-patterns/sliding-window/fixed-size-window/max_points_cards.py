# Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.

# Return the maximum score that can be obtained.

# Example 1
# Input : cardScore = [1, 2, 3, 4, 5, 6] , k = 3
# Output : 15
# Explanation : Choosing the rightmost cards will maximize your total score. So optimal cards chosen are the rightmost three cards 4 , 5 , 6.

# Th score is 4 + 5 + 6 => 15.

# Example 2
# Input : cardScore = [5, 4, 1, 8, 7, 1, 3 ] , k = 3
# Output : 12
# Explanation : In first step we will choose card from beginning with score of 5.
# In second step we will choose the card from beginning again with score of 4.
# In third step we will choose the card from end with score of 3.
# The total score is 5 + 4 + 3 => 12

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from utils import *

class Solution():
    @measure
    def solve(self, params):
        # extract inputs needed for this problem
        cardScore = params["cardScore"]
        k = params["k"]
        
        max_sum = 0
        left_sum = 0
        right_sum = 0

        for i in range(k):
            left_sum = left_sum+cardScore[i]
        
        max_sum = left_sum
        right_index = len(cardScore) - 1

        for i in range(k-1,-1,-1):
            left_sum -= cardScore[i]
            right_sum+=cardScore[right_index]

            max_sum = max(max_sum,left_sum+right_sum)
            right_index-=1

        return max_sum
        

if __name__ == "__main__":
    params = parse_input_file("input.txt")

    result = Solution().solve(params)

    write_output(result)