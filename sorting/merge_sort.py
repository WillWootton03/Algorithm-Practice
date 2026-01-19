numbers = input('Enter numbers seperated by a comma: ')
numbers = [number.strip() for number in numbers.split(',')]

def mergeSort(nums):
    if len(nums) == 1:
        return nums
    
    m = len(nums) // 2
    # Splices nums from index 0 - m and m - end of m
    l = nums[:m]
    r = nums[m:]

    # Recursion for left and right sides 
    l, r = mergeSort(l), mergeSort(r)
    i, j = 0, 0

    index = 0 
    # Our new sorted arr
    a = [0] * len(nums)

    # goes through both halves and combines to sort
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[index] = l[i]
            i += 1
        else:
            a[index] = r[j]
            j += 1

        index += 1
    # Logic for if i or j reaches end of sorted sides
    while i < len(l):
        a[index] = l[i]
        i +=1
        index +=1
    while j < len(r):
        a[index] = r[j]
        j += 1
        index += 1

    return a

print(mergeSort(numbers))
