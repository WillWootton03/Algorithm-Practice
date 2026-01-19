numbers = [1,2,3,4]
target = 3

def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] > target:
            r -=1
        elif numbers[l] + numbers[r] < target:
            l +=1

print(twoSum(numbers, target))