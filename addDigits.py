"""Leverages the Digital Root to perform O(1) for this problem"""
num = 38

def addDigits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

print(addDigits(num))