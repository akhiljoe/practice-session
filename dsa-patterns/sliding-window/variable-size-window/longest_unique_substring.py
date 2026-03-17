# Longest Substring Without Repeating Characters
# Given a string, S. Find the length of the longest substring without repeating characters.


# Example 1
# Input : S = "abcddabac"
# Output : 4
# Explanation : The answer is "abcd" , with a length of 4.

# Example 2
# Input : S = "aaabbbccc"
# Output : 2
# Explanation : The answers are "ab" , "bc". Both have maximum length 2.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from utils import *

class Solution():
    @measure
    def solve(self, params):
        # extract inputs needed for this problem
        S = params["S"]
        mydict = {}
        word = []
        n = len(S)
        
        left = 0
        max_len = 0

        for right in range(n):
            word.append(S[right])
            while S[right] in mydict:
                char = word[left]
                mydict.pop(char)
                left+=1

            mydict[word[right]]=True
            max_len = max(max_len,right-left+1)
        return max_len



if __name__ == "__main__":
    params = parse_input_file("input.txt")

    result = Solution().solve(params)

    write_output(result)




# "abcddabac"

# a,b,c,d,d           a,b,c,d,
# b,c,d,d
# c,d,d
# d,d
# d,a,b,a
# a,b,a
# b,a,c