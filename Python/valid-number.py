from __future__ import print_function
# O(n) runtime, O(1) spacetime.
# Validate if a given string is numeric.
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        s = s.strip()
        length = len(s)
        index = 0
        
        # Deal with symbol
        if index < length and (s[index] == '+' or s[index] == '-'):
            index += 1
        is_normal = False
        is_exp = True
        
        # Deal with digits in the front
        while index < length and s[index].isdigit():
            is_normal = True
            index += 1
            
        # Deal with dot ant digits behind it
        if index < length and s[index] == '.':
            index += 1
            while index < length and s[index].isdigit():
                is_normal = True
                index += 1
                
        # Deal with 'e' and number behind it
        if is_normal and index < length and (s[index] == 'e' or s[index] == 'E'):
            index += 1
            is_exp = False
            if index < length and (s[index] == '+' or s[index] == '-'):
                index += 1
            while index < length and s[index].isdigit():
                index += 1
                is_exp = True
                
        # Return true only deal with all the characters and the part in front of and behind 'e' are all ok
        return is_normal and is_exp and index == length


if __name__ == "__main__":
    print(Solution().isNumber(" 0.1 "))
    print(Solution().isNumber("abc"))
    print(Solution().isNumber("1 a"))
    print(Solution().isNumber("2e10"))
