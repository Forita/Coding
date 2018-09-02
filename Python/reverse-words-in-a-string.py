from __future__ import print_function

# O(n) runtime, O(n) space.
# Given an input string, reverse the string word by word.
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))
    
if __name__ == '__main__':
    print(Solution().reverseWords('the sky is blue'))
