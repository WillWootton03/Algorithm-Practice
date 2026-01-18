numbers = input('Enter numbers seperated by a comma: ')
numbers = [int(number.strip()) for number in numbers.split(',')]

def partition(numbers, lIndex, hIndex):
    m = lIndex + (hIndex - lIndex) / 2
    m = int(m)
    pivot = numbers[m]

    done = False
    while not done:
        while numbers[lIndex] < pivot:
            lIndex += 1
        while pivot < numbers[hIndex]:
            hIndex -= 1
        
        if lIndex >= hIndex:
            done = True
        else:
            numbers[lIndex], numbers[hIndex] = numbers[hIndex], numbers[lIndex]
            lIndex += 1
            hIndex -= 1
    return hIndex

def quicksort(numbers, lIndex, hIndex):
    if lIndex >= hIndex:
        return
    
    lEndIndex = partition(numbers, lIndex, hIndex)

    quicksort(numbers, lIndex, lEndIndex)
    quicksort(numbers, lEndIndex + 1, hIndex)

    return numbers

print(quicksort(numbers, 0, len(numbers)-1))