numbers = input('Enter a list of numbers seperated by a comma: ')
numbers = [int(num.strip()) for num in numbers.split(',')]


def selectionSort(numbers):
    # outer loop iterates over all items in list
    for i in range(len(numbers)):
        # variable to set the base for the smallest number
        sIndex = i
        # iterate over other elements after sIndex
        for j in range(i + 1, len(numbers)):
            # if the current index in unsorted portion is smaller than current smallest number
            if (numbers[j] < numbers[sIndex]):
                # smallest index is replaced by the smallest index in the unsorted list
                sIndex = j
        # after finding the smaller number in the unsorted list swap values
        numbers[i], numbers[sIndex] = numbers[sIndex], numbers[i]

    return numbers

print(selectionSort(numbers))