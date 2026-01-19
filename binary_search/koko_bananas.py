"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
"""

import math
piles = [3,6,7,11]
h = 8

def kokoBananas(piles, h):
    # Get all possible rates between 1 and the max amount in a pil
    l, r = 1, max(piles)
    # Set r to the highest possible rate
    res = r

    while l <= r:
        # get middle reading rate possible
        k = (l + r) // 2
        hours = 0
        for p in piles:
            # Check how many hours it would take to eat said pile of bananas, needs to be ceild per question
            hours += math.ceil(p / k)
        # If she finishes bananas before required time
        if hours <= h:
            # Find the least between res and k
            res = min(res, k)
            # close the window of available eating rates
            r = k - 1
        # If she can't finish in time, increase the window for rate
        else:
            l = k + 1

    return res

print(kokoBananas(piles, h))