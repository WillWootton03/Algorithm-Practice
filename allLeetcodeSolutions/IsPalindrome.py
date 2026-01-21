class Solution:
    def isPalindrome(self, x):
        dig = [d for d in str(x)]
        l, r = 0, len(dig) - 1
        while l <= r:
            if dig[l] == dig[r]:
                l += 1
                r -= 1
            else:
                return False
        return True