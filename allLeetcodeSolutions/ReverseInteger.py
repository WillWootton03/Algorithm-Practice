class Solution:
    def reverse(self, x):
        dig = [d for d in str(x)]
        l, r = 0, len(dig) - 1
        if dig[0] == '-':
            l += 1
        while l < r:
            dig[l], dig[r] = dig[r], dig[l]
            l+=1
            r-=1
        x = int(''.join(dig))
        if x > (2 ** 31) - 1 or x < -(2 ** 31):
            return 0
        else:
            return x