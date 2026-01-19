numbers = input('Enter numbers seperated by a comma: ')
numbers = [int(number.strip()) for number in numbers.split(',')]

def partition(numbers, lIndex, rIndex):
    
    m = lIndex + (rIndex - lIndex) // 2
    pivot = numbers[m]

    done = False
    while not done:
        while numbers[lIndex] < pivot:
            lIndex += 1
        while numbers[rIndex] > pivot:
            rIndex -= 1
        
        if lIndex >= rIndex:
            done = True
        else:
            numbers[lIndex], numbers[rIndex] = numbers[rIndex], numbers[lIndex]
            lIndex += 1
            rIndex -= 1
    return rIndex

def quicksort(numbers, lIndex, rIndex):
    if lIndex >= rIndex:
        return
    
    lEndIndex = partition(numbers, lIndex, rIndex)

    quicksort(numbers, lIndex, lEndIndex)
    quicksort(numbers, lEndIndex + 1, rIndex)

    return numbers

print(quicksort(numbers, 0, len(numbers)-1))